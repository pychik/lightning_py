from __future__ import annotations

from lightning_adapter.api.contexts_api import ContextsApi
from lightning_adapter import EmptyRequest, FrameId, SwitchToFrameRequest
from .mixin import Common
from .window import Window


class Frames(Common):
    def __init__(self, wd):
        super().__init__(wd)
        self._context_instance = ContextsApi(self._api_client)

    def switch_to(self, *, num: int) -> None:
        body = SwitchToFrameRequest(id=num)  # (id=FrameId(num)) not working- too many arguments error
        self._context_instance.switch_to_frame(body=body, session_id=self.session_id)

    def switch_to_parent(self) -> None:
        body = EmptyRequest()
        self._context_instance.switch_to_parent_frame(body=body, session_id=self.session_id)

    def switch_to_default(self):
        body = SwitchToFrameRequest(id=FrameId())
        self._context_instance.switch_to_frame(body=body, session_id=self.session_id)
