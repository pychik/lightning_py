from __future__ import annotations


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
    def context(self):
        return self._wd.context
