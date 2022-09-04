from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime

from lightning_adapter.api.contexts_api import ContextsApi
from lightning_adapter.models import EmptyRequest, SwitchToWindowRequest, Rect


if TYPE_CHECKING:
    from .windows import Windows


class Position:
    def __init__(self, *, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __repr__(self):
        return repr(dict(x=self.x, y=self.y))


class Size:
    def __init__(self, *, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def __repr__(self):
        return repr(dict(width=self.width, height=self.height))


class Window:
    def __init__(self, *, wi: Windows, handle: str):
        self._wi = wi
        self._handle = handle

    @property
    def handle(self):
        return self._handle

    @property
    def size(self) -> Size:
        _rect = self._wi.context_instance.get_window_rect(session_id=self._wi.session_id).value
        return Size(width=_rect.width, height=_rect.height)

    @size.setter
    def size(self, size_set: Size):
        self.switch_to()
        _rect = Rect(width=float(size_set.width), height=float(size_set.height))
        self._wi.context_instance.set_window_rect(body=_rect, session_id=self._wi.session_id)

    @property
    def position(self) -> Position:
        _rect = self._wi.context_instance.get_window_rect(session_id=self._wi.session_id).value
        return Position(x=_rect.x, y=_rect.y)

    @position.setter
    def position(self, position_set: Position):
        self.switch_to()
        _rect = Rect(x=float(position_set.x), y=float(position_set.y))
        self._wi.context_instance.set_window_rect(body=_rect, session_id=self._wi.session_id)

    def close(self) -> Windows:
        self.switch_to()
        self._wi.context_instance.close_window(session_id=self._wi.session_id)
        return self._wi

    def fullscreen(self) -> Window:
        self.switch_to()
        self._wi.context_instance.fullscreen_window(body=EmptyRequest(), session_id=self._wi.session_id)
        return self

    def maximize(self) -> Window:
        self.switch_to()
        self._wi.context_instance.maximize_window(body=EmptyRequest(), session_id=self._wi.session_id)
        return self

    def minimize(self) -> Window:
        self.switch_to()
        self._wi.context_instance.minimize_window(body=EmptyRequest(), session_id=self._wi.session_id)
        return self

    def switch_to(self) -> Window:
        body = SwitchToWindowRequest(handle=self._handle)
        self._wi.context_instance.switch_to_window(body=body, session_id=self._wi.session_id)
        return self
