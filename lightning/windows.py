from __future__ import annotations

from lightning_adapter.api.contexts_api import ContextsApi

from .mixin import Common


class Windows(Common):
    def __init__(self, wd):
        super().__init__(wd)
        self._context_instance = ContextsApi(self._api_client)

    def close_window(self) -> Windows:
        """Closes browser window"""
        self._context_instance.close_window(session_id=self.session_id)
        return self
