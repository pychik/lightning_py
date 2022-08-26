from __future__ import annotations

from datetime import datetime
from lightning_adapter.models import Cookie as RawCookie


class Cookie(dict):

    def __init__(self, *, name: str, value: str, path: str = None,
                 domain: str = None, secure_only: bool = False,
                 http_only: bool = False, expires: datetime = None,
                 same_site_policy: str = None):

        _expires = int(expires.timestamp()) if expires else None
        self._raw = RawCookie(name=name, value=value, path=path,
                              domain=domain, secure=secure_only, http_only=http_only,
                              expiry=_expires, same_site=same_site_policy
                              )

    def raw(self) -> RawCookie:
        return self._raw

    @property
    def name(self) -> str:
        return self._raw.name

    @property
    def value(self) -> str:
        return self._raw.value

    @property
    def path(self) -> str:
        return self._raw.path

    @property
    def domain(self) -> str:
        return self._raw.domain

    @property
    def secure_only(self) -> bool:
        return self._raw.secure

    @property
    def http_only(self) -> bool:
        return self._raw.http_only

    @property
    def expires(self) -> datetime:
        # because of datetime operation we need to check our value
        return datetime.fromtimestamp(self._raw.expiry) if self._raw.expiry else None

    @property
    def same_site_policy(self):
        return self._raw.same_site

    @staticmethod
    def convert_raw(rc: RawCookie) -> Cookie:
        # because of datetime operation we need to check our value
        _ex_val = datetime.fromtimestamp(int(rc.expiry)) if rc.expiry else None

        return Cookie(name=rc.name, value=rc.value,
                      path=rc.path, domain=rc.domain,
                      secure_only=rc.secure, http_only=rc.http_only,
                      expires=_ex_val, same_site_policy=rc.same_site)

    def __repr__(self):
        """This method we use for represantation of our Cookie if user decided to print it"""
        _c = dict(name=self.name, value=self.value, path=self.path,
                  domain=self.domain, secure_only=self.secure_only,
                  http_only=self.http_only, expires=self.expires,
                  same_site_policy=self.same_site_policy)
        return repr(_c)
