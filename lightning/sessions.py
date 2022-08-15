from __future__ import annotations

from typing import Tuple, Optional
from lightning_adapter.api.sessions_api import SessionsApi
from lightning_adapter.models.new_session_request import NewSessionRequest
from lightning_adapter.models.new_session_request_capabilities import NewSessionRequestCapabilities

from .mixin import Common


class Sessions(Common):
    def __init__(self, wd):
        super().__init__(wd)
        self._session_instance = SessionsApi(self._api_client)

        self._session_response, self._session_id = self._get_session()

    @property
    def id(self):
        return self._session_id

    def _get_session(self) -> Tuple[dict, Optional[str]]:
        """Starts the session"""
        body = NewSessionRequest(NewSessionRequestCapabilities(always_match=self._wd.capabilities))
        session_response = self._session_instance.create_session(body)
        # log.info(f"Webdriver started new session with parameters: {session_response.value}")
        return session_response.value, session_response.value.session_id

    @property
    def status(self) -> dict:
        return self._session_instance.get_status().value

    def delete(self) -> None:
        """Finishes the session action"""

        self._session_instance.delete_session(session_id=self.session_id)
