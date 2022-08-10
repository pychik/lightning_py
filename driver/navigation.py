from __future__ import annotations

from swagger_client.api.navigation_api import NavigationApi
from swagger_client.models.empty_request import EmptyRequest
from swagger_client.models.url_request import UrlRequest


class Navigation:
    """Defines Navigation Api"""

    def __init__(self,  wd):
        self._navi_instance = NavigationApi(wd.api_client)
        self._wd = wd

    # Navigation class spec methods
    def navigate(self, url: str) -> Navigation:
        """ Navigates to url"""
        self._navi_instance.navigate_to(session_id=self.session_id, body=UrlRequest(url=url, ))
        return self

    def get_title(self) -> str:
        return self._navi_instance.get_page_title(session_id=self.session_id).value

    def current_url(self) -> str:
        """Returns: str"""
        return self._navi_instance.get_current_url(session_id=self.session_id)

    def back(self) -> Navigation:
        """Navigates to the previous page"""
        self._navi_instance.navigate_back(session_id=self.session_id, body=EmptyRequest())
        return self

    def forward(self) -> Navigation:
        """Navigates to next page"""
        self._navi_instance.navigate_forward(session_id=self.session_id, body=EmptyRequest())
        return self

    # common part of all classes
    @property
    def session_id(self):
        return self._wd.session_id

    @property
    def navigation(self) -> Navigation:
        return self

    @property
    def sessions(self):
        return self._wd.sessions

    @property
    def document(self):
        return self._wd.document

    @property
    def screenshot(self):
        return self._wd.screenshot

    @property
    def context(self):
        return self._wd.context
