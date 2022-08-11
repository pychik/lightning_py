from __future__ import annotations
from typing import TYPE_CHECKING
from swagger_client import ApiClient, Configuration

if TYPE_CHECKING:
    from .context import Context
    from .document import Document
    from .navigation import Navigation
    from .screenshot import Screenshot
    from .sessions import Sessions
    from .timeouts import Timeouts


class Api:
    """Our main class swagger worker api. Singleton"""

    def __init__(self, base_uri: str):
        configuration = Configuration()
        configuration.host = base_uri
        self.api_client = ApiClient(configuration)

    def __new__(cls, base_uri: str):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Api, cls).__new__(cls)
        return cls.instance


class Common:
    def __init__(self, wd):
        # api init with Singleton mechanics
        api = Api(wd.base_uri)
        self._api_client = api.api_client
        self._wd = wd

    @property
    def session_id(self) -> str:
        return self._wd.session_id

    @property
    def navigation(self) -> Navigation:
        return self._wd.navigation

    @property
    def sessions(self) -> Sessions:
        return self._wd.sessions

    @property
    def document(self) -> Document:
        return self._wd.document

    @property
    def screenshot(self) -> Screenshot:
        return self._wd.screenshot

    @property
    def context(self) -> Context:
        return self._wd.context

    @property
    def timeouts(self) -> Timeouts:
        return self._wd.timeouts
