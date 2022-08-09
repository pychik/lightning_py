from __future__ import annotations

import logging as log
from typing import Optional

from swagger_client import ApiClient, Configuration
from swagger_client.api.contexts_api import ContextsApi
from swagger_client.api.document_api import DocumentApi
from swagger_client.api.navigation_api import NavigationApi
from swagger_client.api.screenshots_api import ScreenshotsApi
from swagger_client.api.sessions_api import SessionsApi
# from swagger_client.models.capabilities import Capabilities
from swagger_client.models.empty_request import EmptyRequest
from swagger_client.models.new_session_request import NewSessionRequest
from swagger_client.models.new_session_request_capabilities import NewSessionRequestCapabilities
from swagger_client.models.url_request import UrlRequest

from .capabilities import Capabilities
from .config import Defaults


log.basicConfig(level=log.DEBUG)


class Api:
    """Our main class swagger worker api"""
    def __init__(self, base_uri: str):
        configuration = Configuration()
        configuration.host = base_uri
        self.api_client = ApiClient(configuration)


class Session:
    """Class that defines Sessions Api"""

    # not necessary- only IDE reference
    session_id = ''

    def __init__(self, api_client: ApiClient, capabilities: Capabilities):

        self.capabilities = capabilities
        self.session_instance = SessionsApi(api_client)

    def _get_session(self) -> tuple[dict, Optional[str]]:
        body = NewSessionRequest(NewSessionRequestCapabilities(always_match=self.capabilities))
        session_response = self.session_instance.create_session(body)
        # log.info(f"Webdriver started new session with parameters: {session_response.value}")
        return session_response.value, session_response.value.session_id

    def close(self) -> None:
        """Finishes the session action"""
        self.session_instance.delete_session(session_id=self.session_id)


class Navigation:
    """Defines Navigation Api"""

    # not necessary- only IDE reference
    session_id = ''

    def __init__(self, api_client: ApiClient):
        self.navi_instance = NavigationApi(api_client)

    def get(self, url: str) -> Navigation:
        """ Navigates to url"""
        self.navi_instance.navigate_to(session_id=self.session_id, body=UrlRequest(url=url, ))
        return self

    def get_title(self) -> str:
        return self.navi_instance.get_page_title(session_id=self.session_id).value

    def current_url(self) -> str:
        """Returns: str"""
        return self.navi_instance.get_current_url(session_id=self.session_id)

    def back(self) -> Navigation:
        """Navigates to the previous page"""
        self.navi_instance.navigate_back(session_id=self.session_id, body=EmptyRequest())
        return self

    def forward(self) -> Navigation:
        """Navigates to next page"""
        self.navi_instance.navigate_forward(session_id=self.session_id, body=EmptyRequest())
        return self


class WebDriver(Session, Navigation):
    def __init__(self, base_uri: str = Defaults.BASE_URI,
                 capabilities: Capabilities = Defaults.CAPABILITIES):

        # get our api_client
        api = Api(base_uri)
        self.api_client = api.api_client

        # Open Session (First attempt to divide our api classes)
        Session.__init__(self, self.api_client, capabilities)
        # start session
        self.session_dict, self.session_id = self._get_session()

        # Attempt to divide our api classes
        Navigation.__init__(self, self.api_client)

        # create all needed instances to work with
        self.document_instance = DocumentApi(self.api_client)
        self.context_instance = ContextsApi(self.api_client)
        self.screenshot_instance = ScreenshotsApi(self.api_client)

    def get_page_source(self) -> str:
        return self.document_instance.get_page_source(session_id=self.session_id).value

    def screen_shot(self) -> str:
        """Returns: Dict value: base64 encoded str"""

        return self.screenshot_instance.take_screenshot(session_id=self.session_id).value

    def close_window(self) -> WebDriver:
        """Closes browser window"""
        self.context_instance.close_window(session_id=self.session_id)
        return self

    # def screen_shot_as_png(self, img_path: str) -> Optional[WebDriver]:
    #     img_data = self.screen_shot().value
    #     with open(f"{img_path}.png", "wb") as fh:
    #         try:
    #             fh.write(base64.b64decode(img_data))
    #         except Exception as e:
    #             log.exception(f'Exception occured: {e}')
    #     log.info(f"Screenshot saved to {img_path}")
    #     return self
