from __future__ import annotations

from swagger_client.api.screenshots_api import ScreenshotsApi


class ScreenShot:
    def __init__(self, wd):
        self._screenshot_instance = ScreenshotsApi(wd.api_client)
        self._wd = wd

    def take(self) -> str:
        """Returns: Dict value: base64 encoded str"""

        return self._screenshot_instance.take_screenshot(session_id=self.session_id).value

    @property
    def session_id(self):
        return self._wd.session_id

    @property
    def document(self):
        return self._wd.document

    @property
    def navigation(self):
        return self._wd.navigation

    @property
    def sessions(self):
        return self._wd.sessions

    @property
    def screenshot(self) -> ScreenShot:
        return self

    @property
    def context(self):
        return self._wd.context

# def screenshot_as_png(self, img_path: str) -> Optional[WebDriver]:
    #     img_data = self.screenshot().value
    #     with open(f"{img_path}.png", "wb") as fh:
    #         try:
    #             fh.write(base64.b64decode(img_data))
    #         except Exception as e:
    #             log.exception(f'Exception occured: {e}')
