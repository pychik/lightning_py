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
    def __init__(self, base_uri):
        configuration = Configuration()
        configuration.host = base_uri
        self.api_client = ApiClient(configuration)


class Session(Api):
    """Class that defines Sessions Api"""

    def __init__(self, base_uri, capabilities: Capabilities):
        Api.__init__(self, base_uri)
        self.capabilities = capabilities
        self.session_instance = SessionsApi(self.api_client)

    def _get_session(self) -> tuple[Optional[dict], Optional[str]]:
        body = NewSessionRequest(NewSessionRequestCapabilities(always_match=self.capabilities))
        session_response = self.session_instance.create_session(body)
        # log.info(f"Webdriver started new session with parameters: {session_response.value}")
        return session_response.value, session_response.value.session_id


class WebDriver(Session):
    def __init__(self, base_uri: str = Defaults.BASE_URI,
                 capabilities: Capabilities = Defaults.CAPABILITIES):

        # init our parent class with capabilities not using super() ??
        Session.__init__(self, base_uri, capabilities)


        # create all needed instances to work with
        # start our research of api methods
        self.navi_instance = NavigationApi(self.api_client)
        self.document_instance = DocumentApi(self.api_client)
        self.context_instance = ContextsApi(self.api_client)
        self.screenshot_instance = ScreenshotsApi(self.api_client)

        # start session
        self.session_dict, self.session_id = self._get_session()


    def get(self, url: str) -> Optional[WebDriver]:
        """ Navigates to url"""
        self.navi_instance.navigate_to(session_id=self.session_id, body=UrlRequest(url=url, ))
        return self

    # def send_keys(self):
    #     pass

    def get_page_source(self) -> Optional[dict]:

        return self.document_instance.get_page_source(session_id=self.session_id).value

    def screen_shot(self) -> Optional[dict]:
        """Returns: Dict value: base64 encoded str"""

        return self.screenshot_instance.take_screenshot(session_id=self.session_id).value

    # def screen_shot_as_png(self, img_path: str) -> Optional[WebDriver]:
    #     img_data = self.screen_shot().value
    #     with open(f"{img_path}.png", "wb") as fh:
    #         try:
    #             fh.write(base64.b64decode(img_data))
    #         except Exception as e:
    #             log.exception(f'Exception occured: {e}')
    #     log.info(f"Screenshot saved to {img_path}")
    #     return self

    def current_url(self) -> Optional[str]:
        """Returns: str"""
        return self.navi_instance.get_current_url(session_id=self.session_id)

    def close(self) -> None:
        """Finishes the session action"""
        self.session_instance.delete_session(session_id=self.session_id)

    def back(self) -> Optional[WebDriver]:
        """Navigates to the previous page"""
        self.navi_instance.navigate_back(session_id=self.session_id, body=EmptyRequest())
        return self

    def forward(self) -> Optional[WebDriver]:
        """Navigates to next page"""
        self.navi_instance.navigate_forward(session_id=self.session_id, body=EmptyRequest())
        return self
