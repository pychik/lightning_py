from __future__ import annotations

from swagger_client.api.contexts_api import ContextsApi

from .mixin import Common


class Context(Common):
    def __init__(self, wd):
        self._context_instance = ContextsApi(wd.api_client)
        self._wd = wd

    def close_window(self) -> Context:
        """Closes browser window"""
        self._context_instance.close_window(session_id=self.session_id)
        return self
