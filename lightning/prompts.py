from __future__ import annotations

from lightning_adapter.api.prompts_api import PromptsApi
from lightning_adapter.models import SendAlertTextRequest, EmptyRequest
from .mixin import Common


class Prompts(Common):
    def __init__(self, wd):
        super().__init__(wd)
        self._prompts_instance = PromptsApi(self._api_client)

    @property
    def text(self) -> str:
        return self._prompts_instance.get_alert_text(session_id=self.session_id).value

    @text.setter
    def text(self, text: str) -> None:
        body = SendAlertTextRequest(text=text)
        self._prompts_instance.send_alert_text(body=body, session_id=self.session_id)

    def accept(self) -> Prompts:
        body = EmptyRequest()
        self._prompts_instance.accept_alert(body=body, session_id=self.session_id)
        return self

    def dismiss(self) -> Prompts:
        body = EmptyRequest()
        self._prompts_instance.dismiss_alert(body=body, session_id=self.session_id)
        return self
