import logging as log

from .capabilities import Capabilities
from .windows import Windows
from .cookies import Cookies
from .elements import Elements
from .frames import Frames
from .document import Document
from .navigation import Navigation
from .prompts import Prompts
from .print import Print
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
        self._cookies = Cookies(wd=self)
        self._elements = Elements(wd=self)
        self._frames = Frames(wd=self)
        self._navigation = Navigation(wd=self)
        self._prompts = Prompts(wd=self)
        self._print = Print(wd=self)
        self._document = Document(wd=self)
        self._screenshot = Screenshot(wd=self)
        self._windows = Windows(wd=self)
        self._timeouts = Timeouts(wd=self)

    @property
    def session_id(self) -> str:
        return self._sessions.id

    @property
    def navigation(self) -> Navigation:
        return self._navigation

    @property
    def prompts(self) -> Prompts:
        return self._prompts

    @property
    def print(self) -> Print:
        return self._print

    @property
    def sessions(self) -> Sessions:
        return self._sessions

    @property
    def cookies(self) -> Cookies:
        return self._cookies

    @property
    def elements(self) -> Elements:
        return self._elements

    @property
    def frames(self) -> Frames:
        return self._frames

    @property
    def document(self) -> Document:
        return self._document

    @property
    def screenshot(self) -> Screenshot:
        return self._screenshot

    @property
    def windows(self) -> Windows:
        return self._windows

    @property
    def timeouts(self) -> Timeouts:
        return self._timeouts
