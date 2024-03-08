"""contains the actual client"""

import asyncio
import logging
import uuid
from typing import AsyncGenerator, Callable, Literal, Optional, overload

from aiohttp import BasicAuth, ClientResponseError, ClientSession, ClientTimeout
from more_itertools import chunked
from yarl import URL

from tmdsclient.client.config import TmdsConfig
from tmdsclient.models import AllIdsResponse
from tmdsclient.models.netzvertrag import Netzvertrag, _ListOfNetzvertraege
from tmdsclient.models.patches import build_json_patch_document

_logger = logging.getLogger(__name__)

_DEFAULT_CHUNK_SIZE = 100


class TmdsClient:
    """
    an async wrapper around the TMDS API
    """

    def __init__(self, config: TmdsConfig):
        self._config = config
        self._auth = BasicAuth(login=self._config.usr, password=self._config.pwd)
        self._session_lock = asyncio.Lock()
        self._session: Optional[ClientSession] = None
        _logger.info("Instantiated TmdsClient with server_url %s", str(self._config.server_url))

    def get_top_level_domain(self) -> URL | None:
        """
        Returns the top level domain of the server_url; this is useful to differentiate prod from test systems.
        If the server_url is an IP address, None is returned.
        """
        # this method is unit tested; check the testcases to understand its branches
        domain_parts = self._config.server_url.host.split(".")  # type:ignore[union-attr]
        if all(x.isnumeric() for x in domain_parts):
            # seems like this is an IP address
            return None
        if not any(domain_parts):
            return self._config.server_url
        tld: str
        if domain_parts[-1] == "localhost":
            tld = ".".join(domain_parts[-1:])
        else:
            tld = ".".join(domain_parts[-2:])
        return URL(self._config.server_url.scheme + "://" + tld)

    async def _get_session(self) -> ClientSession:
        """
        returns a client session (that may be reused or newly created)
        re-using the same (threadsafe) session will be faster than re-creating a new session for every request.
        see https://docs.aiohttp.org/en/stable/http_request_lifecycle.html#how-to-use-the-clientsession
        """
        async with self._session_lock:
            if self._session is None or self._session.closed:
                _logger.info("creating new session")
                self._session = ClientSession(
                    auth=self._auth,
                    timeout=ClientTimeout(60),
                    raise_for_status=True,
                )
            else:
                _logger.log(5, "reusing aiohttp session")  # log level 5 is half as "loud" logging.DEBUG
            return self._session

    async def close_session(self):
        """
        closes the client session
        """
        async with self._session_lock:
            if self._session is not None and not self._session.closed:
                _logger.info("Closing aiohttp session")
                await self._session.close()
                self._session = None

    async def get_netzvertraege_for_melo(self, melo_id: str) -> list[Netzvertrag]:
        """
        provide a melo id, e.g. 'DE1234567890123456789012345678901' and get the corresponding netzvertrag
        """
        if not melo_id:
            raise ValueError("You must not provide an empty melo_id")
        session = await self._get_session()
        request_url = self._config.server_url / "api" / "Netzvertrag" / "find" % {"messlokation": melo_id}
        request_uuid = uuid.uuid4()
        _logger.debug("[%s] requesting %s", str(request_uuid), request_url)
        async with session.get(request_url) as response:
            response.raise_for_status()  # endpoint returns an empty list but no 404
            _logger.debug("[%s] response status: %s", str(request_uuid), response.status)
            response_json = await response.json()
            _list_of_netzvertraege = _ListOfNetzvertraege.model_validate(response_json)
        return _list_of_netzvertraege.root

    async def get_netzvertrag_by_id(self, nv_id: uuid.UUID) -> Netzvertrag | None:
        """
        provide a UUID, get the matching netzvertrag in return (or None, if 404)
        """
        session = await self._get_session()
        request_url = self._config.server_url / "api" / "Netzvertrag" / str(nv_id)
        request_uuid = uuid.uuid4()
        _logger.debug("[%s] requesting %s", str(request_uuid), request_url)
        async with session.get(request_url) as response:
            try:
                if response.status == 404:
                    return None
                response.raise_for_status()
            finally:
                _logger.debug("[%s] response status: %s", str(request_uuid), response.status)
            response_json = await response.json()
            result = Netzvertrag.model_validate(response_json)
        return result

    async def get_all_netzvertrag_ids(self) -> list[uuid.UUID]:
        """
        get all IDs of netzverträge that exist on server side
        """
        session = await self._get_session()
        request_url = self._config.server_url / "api" / "Netzvertrag" / "allIds"
        request_uuid = uuid.uuid4()
        _logger.debug("[%s] requesting %s", str(request_uuid), request_url)
        async with session.get(request_url) as response:
            response.raise_for_status()
            _logger.debug("[%s] response status: %s", str(request_uuid), response.status)
            response_json = await response.json()
            all_ids_response = AllIdsResponse.model_validate(response_json)
        result = [uuid.UUID(x.interne_id) for x in all_ids_response.root["Netzvertrag"]]
        _logger.info("There are %i Netzvertraege on server side", len(result))
        return result

    @overload
    async def get_all_netzvertraege(
        self, as_generator: Literal[False], chunk_size: int = _DEFAULT_CHUNK_SIZE
    ) -> list[Netzvertrag]: ...

    @overload
    async def get_all_netzvertraege(
        self, as_generator: Literal[True], chunk_size: int = _DEFAULT_CHUNK_SIZE
    ) -> AsyncGenerator[Netzvertrag, None]: ...

    async def get_all_netzvertraege(
        self, as_generator: bool, chunk_size: int = _DEFAULT_CHUNK_SIZE
    ) -> list[Netzvertrag] | AsyncGenerator[Netzvertrag, None]:
        """
        download all netzverträge from TMDS
        """
        all_ids = await self.get_all_netzvertrag_ids()

        def _log_chunk_success(chunk_idx: int, chunk_length: int) -> None:
            _logger.debug(
                "Downloaded Netzvertrag (%i/%i) / chunk %i/%i",
                chunk_size * chunk_idx + chunk_length,
                len(all_ids),
                chunk_idx + 1,
                len(all_ids) // chunk_size + 1,
            )

        if as_generator:

            async def generator():
                successfully_downloaded = 0
                for chunk_index, id_chunk in enumerate(chunked(all_ids, chunk_size)):
                    get_tasks = [self.get_netzvertrag_by_id(nv_id) for nv_id in id_chunk]
                    try:
                        result_chunk = await asyncio.gather(*get_tasks)
                        for nv in result_chunk:
                            yield nv
                            successfully_downloaded += 1
                    except ClientResponseError as chunk_client_error:
                        if chunk_client_error.status != 500:
                            raise
                        _logger.warning("Failed to download chunk %i; Retrying one by one", chunk_index)
                        for nv_id in id_chunk:
                            # This is a bit dumb; If we had aiostream here, we could create multiple requests at once
                            # and yield from a merged stream. This might be a future improvement... For now it's ok.
                            # With a moderate sized chunk_size it should be fine as there are not that many 500 errors.
                            try:
                                yield await self.get_netzvertrag_by_id(nv_id)
                                successfully_downloaded += 1
                            except ClientResponseError as single_client_error:
                                if single_client_error.status != 500:
                                    raise
                                _logger.exception("Failed to download Netzvertrag %s; skipping", nv_id)
                                continue
                _logger.info("Successfully downloaded %i Netzvertraege", successfully_downloaded)

            return generator()  # This needs to be called to return an AsyncGenerator
        result: list[Netzvertrag] = []
        for chunk_index, id_chunk in enumerate(chunked(all_ids, chunk_size)):
            # we probably need to account for the fact that this leads to HTTP 500 errors, let's see
            get_tasks = [self.get_netzvertrag_by_id(nv_id) for nv_id in id_chunk]
            try:
                result_chunk = await asyncio.gather(*get_tasks)
            except ClientResponseError as chunk_client_error:
                if chunk_client_error.status != 500:
                    raise
                _logger.warning("Failed to download chunk %i; Retrying 1 by 1", chunk_index)
                result_chunk = []
                for nv_id in id_chunk:
                    try:
                        nv = await self.get_netzvertrag_by_id(nv_id)
                    except ClientResponseError as single_client_error:
                        if single_client_error.status != 500:
                            raise
                        _logger.exception("Failed to download Netzvertrag %s; skipping", nv_id)
                        continue
                    assert nv is not None
                    result_chunk.append(nv)
            if any(x is None for x in result_chunk):
                raise ValueError("This must not happen.")
            _log_chunk_success(chunk_index, len(result_chunk))
            result.extend(result_chunk)  # type:ignore[arg-type]
        _logger.info("Successfully downloaded %i Netzvertraege", len(result))
        return result

    async def update_netzvertrag(
        self, netzvertrag_id: uuid.UUID, changes: list[Callable[[Netzvertrag], None]]
    ) -> Netzvertrag:
        """
        patch the given netzvertrag using the changes
        """
        session = await self._get_session()
        netzvertrag = await self.get_netzvertrag_by_id(netzvertrag_id)
        if netzvertrag is None:
            raise ValueError(f"Netzvertrag with id {netzvertrag_id} not found")
        patch_document = build_json_patch_document(netzvertrag, changes)
        request_url = self._config.server_url / "api" / "v2" / "Netzvertrag" / str(netzvertrag_id)
        request_uuid = uuid.uuid4()
        _logger.debug("[%s] requesting %s", str(request_uuid), request_url)
        async with session.patch(
            request_url, json=patch_document.patch, headers={"Content-Type": "application/json-patch+json"}
        ) as response:
            response.raise_for_status()
            _logger.debug("[%s] response status: %s", str(request_uuid), response.status)
            response_json = await response.json()
            result = Netzvertrag.model_validate(response_json)
        return result
