from __future__ import annotations

from swagger_client.api.contexts_api import ContextsApi


class Context:
    def __init__(self, wd):
        self._context_instance = ContextsApi(wd.api_client)
        self._wd = wd

    def close_window(self) -> Context:
        """Closes browser window"""
        self._context_instance.close_window(session_id=self.session_id)
        return self

    @property
    def session_id(self):
        return self._wd.session_id

    @property
    def document(self):
        return self._wd.document

    @property
    def navigation(self):
        return self._wd.navigation

    @property
    def sessions(self):
        return self._wd.sessions

    @property
    def screenshot(self):
        return self._wd.screenshot

    @property
    def context(self) -> Context:
        return self
