from __future__ import annotations

from base64 import b64decode
from swagger_client.api.screenshots_api import ScreenshotsApi

from .mixin import Common


class Screenshot(Common):
    """Defines Screenshot Api"""

    def __init__(self, wd):
        super().__init__(wd)
        self._screenshot_instance = ScreenshotsApi(self._api_client)

    def take(self) -> bytes:
        """Returns: bytes of image"""

        return b64decode(self._screenshot_instance.take_screenshot(session_id=self.session_id).value)
