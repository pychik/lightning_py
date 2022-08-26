from __future__ import annotations

from lightning_adapter.api.cookies_api import CookiesApi
from lightning_adapter.models import CookieRequest

from .mixin import Common
from .cookie import Cookie


class Cookies(Common):
    def __init__(self, wd):
        super().__init__(wd)
        self._cookies_instance = CookiesApi(self._api_client)

    @property
    def all(self) -> list[Cookie]:
        lc = self._cookies_instance.get_all_cookies(session_id=self.session_id).value
        list_cookies = [Cookie.convert_raw(c) for c in lc]
        return list_cookies

    @all.deleter
    def all(self) -> Cookies:
        self._cookies_instance.delete_all_cookies(session_id=self.session_id)
        return self

    def get(self, name: str) -> Cookie:
        c = self._cookies_instance.get_named_cookie(session_id=self.session_id, name=name).value
        return Cookie.convert_raw(c)

    def delete(self, name: str) -> Cookies:
        self._cookies_instance.delete_cookie(session_id=self.session_id, name=name)
        return self

    def add(self, cookie: Cookie) -> Cookies:
        self._cookies_instance.add_cookie(body=CookieRequest(cookie=cookie.raw()), session_id=self.session_id)
        return self
