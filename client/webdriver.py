import logging as log

from .capabilities import Capabilities
from .context import Context
from .document import Document
from .navigation import Navigation
from .screenshot import Screenshot
from .sessions import Sessions
from .timeouts import Timeouts

log.basicConfig(level=log.DEBUG)


class WebDriver:
    """WebDriver class uniting all W3C classes and there methods"""

    def __init__(self, base_uri: str, capabilities: Capabilities):
        self.base_uri = base_uri
        self.capabilities = capabilities

        self._sessions = Sessions(wd=self)
        self._navigation = Navigation(wd=self)
        self._document = Document(wd=self)
        self._screenshot = Screenshot(wd=self)
        self._context = Context(wd=self)
        self._timeouts = Timeouts(wd=self)

    @property
    def session_id(self) -> str:
        return self._sessions.id

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
    def screenshot(self) -> Screenshot:
        return self._screenshot

    @property
    def context(self) -> Context:
        return self._context

    @property
    def timeouts(self) -> Timeouts:
        return self._timeouts
