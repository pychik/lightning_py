from __future__ import annotations

from typing import Tuple, Optional
from swagger_client.api.sessions_api import SessionsApi
from swagger_client.models.new_session_request import NewSessionRequest
from swagger_client.models.new_session_request_capabilities import NewSessionRequestCapabilities

from .mixin import Common


class Sessions(Common):
    def __init__(self, wd):
        self.capabilities = wd.capabilities
        self._session_instance = SessionsApi(wd.api_client)
        self._wd = wd
        self._session_response, self._session_id = self._get_session()

    @property
    def session_id(self):
        return self._session_id

    def _get_session(self) -> Tuple[dict, Optional[str]]:
        body = NewSessionRequest(NewSessionRequestCapabilities(always_match=self.capabilities))
        session_response = self._session_instance.create_session(body)
        # log.info(f"Webdriver started new session with parameters: {session_response.value}")
        return session_response.value, session_response.value.session_id

    @property
    def status(self) -> dict:
        return self._session_instance.get_status().value

    def close(self) -> None:
        """Finishes the session action"""

        self._session_instance.delete_session(session_id=self.session_id)
        print(self.session_id, "closed")
