from __future__ import annotations

from swagger_client.api.document_api import DocumentApi


class Document:
    def __init__(self, wd):
        self._wd = wd
        self._document_instance = DocumentApi(wd.api_client)

    # @property
    def get_page_source(self) -> str:
        return self._document_instance.get_page_source(session_id=self.session_id).value

    @property
    def session_id(self):
        return self._wd.session_id

    @property
    def document(self) -> Document:
        return self

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
    def context(self):
        return self._wd.context
