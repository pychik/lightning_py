from __future__ import annotations

from lightning_adapter.api.navigation_api import NavigationApi
from lightning_adapter.models.empty_request import EmptyRequest
from lightning_adapter.models.url_request import UrlRequest

from .mixin import Common


class Navigation(Common):
    """Defines Navigation Api"""

    def __init__(self,  wd):
        super().__init__(wd)
        self._navi_instance = NavigationApi(self._api_client)

    @property
    def get_title(self) -> str:
        return self._navi_instance.get_page_title(session_id=self.session_id).value

    @property
    def current_url(self) -> str:
        """Returns: str"""
        return self._navi_instance.get_current_url(session_id=self.session_id)

    # Navigation class spec methods
    def navigate(self, url: str) -> Navigation:

        """ Navigates to url"""
        self._navi_instance.navigate_to(session_id=self.session_id, body=UrlRequest(url=url, ))
        return self

    def refresh(self) -> Navigation:
        self._navi_instance.refresh_page(session_id=self.session_id, body=UrlRequest(url=self.current_url))
        return self

    def back(self) -> Navigation:
        """Navigates to the previous page"""
        self._navi_instance.navigate_back(session_id=self.session_id, body=EmptyRequest())
        return self

    def forward(self) -> Navigation:
        """Navigates to next page"""
        self._navi_instance.navigate_forward(session_id=self.session_id, body=EmptyRequest())
        return self
