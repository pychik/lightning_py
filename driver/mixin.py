from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .context import Context
    from .document import Document
    from .navigation import Navigation
    from .screenshot import ScreenShot
    from .sessions import Sessions


class Common:
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
    def screenshot(self) -> ScreenShot:
        return self._wd.screenshot

    @property
    def context(self) -> Context:
        return self._wd.context
