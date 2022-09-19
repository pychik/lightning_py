from __future__ import annotations

from typing import Optional

from lightning_adapter.api.contexts_api import ContextsApi
from lightning_adapter import EmptyRequest, FrameId, SwitchToFrameRequest

from .exceptions import WebDriverException
from .mixin import Common
from .webelement import WebElement


class Frames(Common):
    def __init__(self, wd):
        super().__init__(wd)
        self._context_instance = ContextsApi(self._api_client)

    def switch_to(self, index: int = None, element: WebElement = None):
        if index and not element:
            body = SwitchToFrameRequest(id=index)
            self._context_instance.switch_to_frame(body=body, session_id=self.session_id)
        if element and not index:
            _id: dict = {"element-6066-11e4-a52e-4f735466cecf": element.id}
            body = SwitchToFrameRequest(id=_id)
            self._context_instance.switch_to_frame(body=body, session_id=self.session_id)
        if index and element:
            raise WebDriverException(message=f"Invalid input arguments passed to {self.__class__.__name__}. "
                                     f"Enter only one of arguments not both", errors="Frames error")

        if index is None and element is None:
            raise WebDriverException(message=f"Invalid blank input arguments passed to {self.__class__.__name__}. "
                                             f"Enter one of arguments", errors="Frames error")

    def switch_to_parent(self) -> None:
        body = EmptyRequest()
        self._context_instance.switch_to_parent_frame(body=body, session_id=self.session_id)

    def switch_to_default(self):
        body = SwitchToFrameRequest()
        self._context_instance.switch_to_frame(body=body, session_id=self.session_id)
