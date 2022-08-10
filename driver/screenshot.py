from __future__ import annotations

from swagger_client.api.screenshots_api import ScreenshotsApi

from .mixin import Common


class ScreenShot(Common):
    def __init__(self, wd):
        self._screenshot_instance = ScreenshotsApi(wd.api_client)
        self._wd = wd

    def take(self) -> str:
        """Returns: Dict value: base64 encoded str"""

        return self._screenshot_instance.take_screenshot(session_id=self.session_id).value
