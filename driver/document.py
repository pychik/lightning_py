from __future__ import annotations

from swagger_client.api.document_api import DocumentApi

from .mixin import Common


class Document(Common):
    def __init__(self, wd):
        self._wd = wd
        self._document_instance = DocumentApi(self._wd.api_client)

    # @property
    def get_page_source(self) -> str:
        return self._document_instance.get_page_source(session_id=self.session_id).value
