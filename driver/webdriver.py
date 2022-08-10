from __future__ import annotations

import logging as log

from swagger_client import ApiClient, Configuration

from .capabilities import Capabilities
from .config import Defaults
from .context import Context
from .document import Document
from .navigation import Navigation
from .screenshot import ScreenShot
from .sessions import Sessions


log.basicConfig(level=log.DEBUG)


class Api:
    """Our main class swagger worker api"""
    def __init__(self, base_uri: str):
        configuration = Configuration()
        configuration.host = base_uri
        self.api_client = ApiClient(configuration)


class WebDriver:

    # _session_id: str
    # _navigation: Navigation
    # _sessions: Sessions
    # _document: Document
    # _screenshot: ScreenShot
    # _context: Context

    def __init__(self, base_uri: str = Defaults.BASE_URI, capabilities: Capabilities = Defaults.CAPABILITIES):
        # get our api_client
        api = Api(base_uri)
        self.api_client = api.api_client
        self.capabilities = capabilities

        self._sessions = Sessions(wd=self)

        self._navigation = Navigation(wd=self)
        self._document = Document(wd=self)
        self._screenshot = ScreenShot(wd=self)
        self._context = Context(wd=self)

    @property
    def session_id(self) -> str:
        return self._sessions.session_id

    @property
    def navigation(self) -> Navigation:
        return self._navigation

    @property
    def sessions(self) -> Sessions:
        return self._sessions

    @property
    def document(self) -> Document:
        return self._document

    @property
    def screenshot(self) -> ScreenShot:
        return self._screenshot

    @property
    def context(self) -> Context:
        return self._context
