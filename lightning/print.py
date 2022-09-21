from __future__ import annotations

from base64 import b64decode
from typing import Optional

from lightning_adapter.api.print_api import PrintApi
from lightning_adapter.models import PrintRequest, PrintRequestOptions,\
                                     PrintRequestOptionsPage, PrintRequestOptionsMargin

from .config import Settings
from .mixin import Common


class PrintSettings:
    pages = []

    def __init__(self, width: float = None, height: float = None, scale: float = Settings.PRINT_SCALE_DEFAULT,
                 original_size: bool = True, landscape: str = Settings.PRINT_LANDSCAPE_DEFAULT,
                 margin_top: float = None, margin_left: float = None, margin_right: float = None,
                 margin_bottom: float = None):

        self._width = width
        self._height = height
        self._scale = scale
        self._original_size = original_size
        self._landscape = landscape
        self._margin_top = margin_top
        self._margin_left = margin_left
        self._margin_right = margin_right
        self._margin_bottom = margin_bottom

    @property
    def width(self) -> Optional[float]:
        return self._width

    @width.setter
    def width(self, value: Optional[float]) -> None:
        self._width = value

    @property
    def height(self) -> Optional[float]:
        return self._height

    @height.setter
    def height(self, value: Optional[float]) -> None:
        self._height = value

    @property
    def scale(self) -> float:
        return self._scale

    @scale.setter
    def scale(self, value: float) -> None:
        self._scale = value

    @property
    def original_size(self) -> Optional[bool]:
        return self._original_size

    @original_size.setter
    def original_size(self, value: Optional[float]) -> None:
        self._original_size = value

    @property
    def landscape(self) -> str:
        return self._landscape

    @landscape.setter
    def landscape(self, value: str) -> None:
        self._landscape = value

    @property
    def margin_top(self) -> Optional[float]:
        return self._margin_top

    @margin_top.setter
    def margin_top(self, value: Optional[float]) -> None:
        self._margin_top = value

    @property
    def margin_bottom(self) -> Optional[float]:
        return self._margin_bottom

    @margin_bottom.setter
    def margin_bottom(self, value: Optional[float]) -> None:
        self._margin_bottom = value

    @property
    def margin_left(self) -> Optional[float]:
        return self._margin_left

    @margin_left.setter
    def margin_left(self, value: Optional[float]) -> None:
        self._margin_left = value

    @property
    def margin_right(self) -> Optional[float]:
        return self._margin_right

    @margin_right.setter
    def margin_right(self, value: Optional[float]) -> None:
        self._margin_right = value

    def add_pages(self, page_number: Optional[str, int]) -> PrintSettings:
        self.pages.append(str(page_number))
        return self

    def __repr__(self):
        _c = dict(width=self.width, height=self.height,
                  scale=self.scale, original_size=self.original_size,
                  landscape=self.landscape, margin_top=self.margin_top,
                  margin_bottom=self.margin_bottom, margin_left=self.margin_left,
                  margin_right=self.margin_right, pages=self.pages)
        return repr(_c)


class Print(Common):
    def __init__(self, wd):
        super().__init__(wd)
        self._print_instance = PrintApi(self._api_client)

    @staticmethod
    def _print_request_options(print_settings: PrintSettings) -> PrintRequestOptions:
        _page = PrintRequestOptionsPage(width=print_settings.width, height=print_settings.height)
        _margin = PrintRequestOptionsMargin(top=print_settings.margin_top, bottom=print_settings.margin_bottom,
                                            left=print_settings.margin_left, right=print_settings.margin_right)

        # there is another field <background> should we operate with it?
        _options = PrintRequestOptions(orientation=print_settings.landscape,
                                       scale=print_settings.scale,
                                       page=_page,
                                       margin=_margin,
                                       shrink_to_fit=print_settings.original_size,
                                       page_ranges=print_settings.pages)
        return _options

    def pdf(self, settings: PrintSettings) -> bytes:
        print_options = self._print_request_options(print_settings=settings)
        body = PrintRequest(options=print_options)
        return b64decode(self._print_instance.print_page(body=body, session_id=self.session_id).value)
