from __future__ import annotations

from lightning_adapter.api.contexts_api import ContextsApi
from lightning_adapter import NewWindowRequest
from typing import Optional, Union
from .mixin import Common
from .window import Window


class Windows(Common):
    def __init__(self, wd):
        super().__init__(wd)
        self._context_instance = ContextsApi(self._api_client)

    @property
    def context_instance(self) -> ContextsApi:
        return self._context_instance

    def list(self):
        _handles = self._context_instance.get_window_handles(session_id=self.session_id).value
        return list(map(lambda x: Window(wi=self, handle=x), _handles))

    def _create_window(self, add_type: str) -> Window:
        body = NewWindowRequest(type=add_type)
        handle = self._context_instance.create_new_window(body=body, session_id=self.session_id).value.handle
        return Window(wi=self, handle=handle)

    def create_window(self) -> Window:
        return self._create_window(add_type='window')

    def create_tab(self) -> Window:
        return self._create_window(add_type='tab')

    def current(self) -> Window:
        handle = self._context_instance.get_window_handle(session_id=self.session_id).value
        return Window(wi=self, handle=handle)
