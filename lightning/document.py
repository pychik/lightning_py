from __future__ import annotations

from lightning_adapter.api.document_api import DocumentApi
from lightning_adapter.models.any_response import AnyResponse
from lightning_adapter.models.script_request import ScriptRequest

from .mixin import Common


class Document(Common):
    def __init__(self, wd):
        super().__init__(wd)
        self._document_instance = DocumentApi(self._api_client)

    @property
    def page_source(self) -> str:
        return self._document_instance.get_page_source(session_id=self.session_id).value

    def execute_async_script(self, script: str, *args) -> AnyResponse:
        body = ScriptRequest(script=script, args=[*args])
        r = self._document_instance.execute_script_async(body, session_id=self.session_id, async_req=True)
        return r.get().value

    def execute_script(self, script: str, *args) -> AnyResponse:
        body = ScriptRequest(script=script, args=[*args])
        r = self._document_instance.execute_script(body, session_id=self.session_id)
        return r.value

