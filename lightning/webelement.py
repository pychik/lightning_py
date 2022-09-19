from __future__ import annotations

from base64 import b64decode
from typing import Optional

from lightning_adapter.api.elements_api import ElementsApi
from lightning_adapter.api.screenshots_api import ScreenshotsApi
from lightning_adapter.models import LocatorStrategy, EmptyRequest, FindElementRequest,\
                                      FindElementResponseValue, Rect, ElementSendKeysRequest

from .exceptions import WEB_ELEMENT_ERROR, webdriver_exception
from .window import Position, Size


class Locator:

    def __init__(self, expression: str, strategy: LocatorStrategy):
        self._expression = expression
        self._strategy = strategy

    @property
    def expression(self) -> str:
        return self._expression

    @property
    def strategy(self) -> LocatorStrategy:
        return self._strategy


class By(Locator):

    @staticmethod
    def css_selector(selector: str) -> By:
        return By(expression=selector, strategy=LocatorStrategy.CSS_SELECTOR)

    @staticmethod
    def xpath(selector: str) -> By:
        return By(expression=selector, strategy=LocatorStrategy.XPATH)

    @staticmethod
    def tag_name(selector: str) -> By:
        return By(expression=selector, strategy=LocatorStrategy.TAG_NAME)

    @staticmethod
    def link_text(selector: str) -> By:
        return By(expression=selector, strategy=LocatorStrategy.LINK_TEXT)

    @staticmethod
    def partial_link_text(selector: str) -> By:
        return By(expression=selector, strategy=LocatorStrategy.PARTIAL_LINK_TEXT)


class Accessibility(dict):
    def __init__(self, elements_instance: ElementsApi, session_id: str, id: str):
        self._elements_instance = elements_instance
        self._session_id = session_id
        self._id = id

    @property
    def role(self) -> str:
        _role = self._elements_instance\
            .get_element_computed_role(session_id=self._session_id, element_id=self._id).value
        return _role

    @property
    def label(self) -> str:
        _label = self._elements_instance\
            .get_element_computed_label(session_id=self._session_id, element_id=self._id).value
        return _label

    def __repr__(self):
        _c = dict(role=self.role, label=self.label)
        return repr(_c)


class WebElement(dict):

    def __init__(self, elements_instance: ElementsApi, id: str, session_id: str):
        self._elements_instance = elements_instance
        self._id = id
        self._session_id = session_id

    def accessibility(self) -> Accessibility:
        _accessibility = Accessibility(elements_instance=self._elements_instance,
                                       session_id=self.session_id,
                                       id=self.id)
        return _accessibility

    @property
    def id(self) -> str:
        return self._id

    @property
    def session_id(self) -> str:
        return self._session_id

    @webdriver_exception(WEB_ELEMENT_ERROR)
    def click(self) -> WebElement:
        _web_element = self._elements_instance.element_click(session_id=self.session_id,
                                                             element_id=self.id,
                                                             body=EmptyRequest())
        return self

    @webdriver_exception(WEB_ELEMENT_ERROR)
    def clear(self) -> WebElement:
        _web_element = self._elements_instance.element_clear(session_id=self.session_id,
                                                             element_id=self.id,
                                                             body=EmptyRequest())

        return self

    @webdriver_exception(WEB_ELEMENT_ERROR)
    def find_all(self, locator: Locator) -> list[WebElement]:
        _body = FindElementRequest(using=locator.strategy, value=locator.expression)
        _response: list[FindElementResponseValue] = self._elements_instance.find_elements(session_id=self.session_id,
                                                                                          body=_body).value
        _web_elements = list(map(lambda e: WebElement(elements_instance=self._elements_instance,
                                                      id=e.element_6066_11e4_a52e_4f735466cecf,
                                                      session_id=self.session_id), _response))
        return _web_elements

    @webdriver_exception(WEB_ELEMENT_ERROR)
    def find_first(self, locator: Locator) -> WebElement:
        _body = FindElementRequest(using=locator.strategy, value=locator.expression)
        _response: FindElementResponseValue = self._elements_instance.find_element(session_id=self.session_id,
                                                                                   body=_body).value
        _web_element = WebElement(elements_instance=self._elements_instance,
                                  id=_response.element_6066_11e4_a52e_4f735466cecf,
                                  session_id=self.session_id)
        return _web_element

    @property
    @webdriver_exception(WEB_ELEMENT_ERROR)
    def selected(self) -> bool:
        return self._elements_instance.is_element_selected(session_id=self.session_id, element_id=self.id).value

    @property
    @webdriver_exception(WEB_ELEMENT_ERROR)
    def enabled(self) -> bool:
        return self._elements_instance.is_element_enabled(session_id=self.session_id, element_id=self.id).value

    @property
    @webdriver_exception(WEB_ELEMENT_ERROR)
    def displayed(self) -> bool:
        return self._elements_instance.is_element_displayed(session_id=self.session_id, element_id=self.id).value

    @webdriver_exception(WEB_ELEMENT_ERROR)
    def attribute(self, name: str) -> Optional[str]:
        _response = self._elements_instance.get_element_attribute(session_id=self.session_id,
                                                                  element_id=self.id,
                                                                  name=name)
        return _response.value

    @property
    @webdriver_exception(WEB_ELEMENT_ERROR)
    def position(self) -> Position:
        _rect_response: Rect = self._elements_instance.get_element_rect(session_id=self.session_id,
                                                                        element_id=self.id).value
        return Position(x=int(_rect_response.x), y=int(_rect_response.y))

    @property
    @webdriver_exception(WEB_ELEMENT_ERROR)
    def size(self) -> Size:
        _rect_response: Rect = self._elements_instance.get_element_rect(session_id=self.session_id,
                                                                        element_id=self.id).value
        return Size(width=int(_rect_response.width), height=int(_rect_response.height))

    @webdriver_exception(WEB_ELEMENT_ERROR)
    def element_property(self, name: str) -> Optional[str]:
        _response = self._elements_instance.get_element_property(session_id=self.session_id,
                                                                 element_id=self.id,
                                                                 name=name)
        return _response.value

    @webdriver_exception(WEB_ELEMENT_ERROR)
    def css_property(self, name) -> str:
        _response = self._elements_instance.get_element_css_property(session_id=self.session_id,
                                                                     element_id=self.id,
                                                                     property_name=name)
        return _response.value

    @property
    @webdriver_exception(WEB_ELEMENT_ERROR)
    def tag_name(self) -> str:
        _response = self._elements_instance.get_element_tag_name(session_id=self.session_id, element_id=self.id)
        return _response.value

    @property
    @webdriver_exception(WEB_ELEMENT_ERROR)
    def text(self) -> str:
        _response = self._elements_instance.get_element_text(session_id=self.session_id, element_id=self.id)
        return _response.value

    @webdriver_exception(WEB_ELEMENT_ERROR)
    def send_keys(self, text: str) -> WebElement:
        body = ElementSendKeysRequest(text=text)
        _request = self._elements_instance.element_send_keys(body=body,
                                                             session_id=self.session_id,
                                                             element_id=self.id)
        return self

    @webdriver_exception(WEB_ELEMENT_ERROR)
    def screenshot(self) -> bytes:
        _api_client = self._elements_instance.api_client
        _screenshot_instance = ScreenshotsApi(_api_client)
        return b64decode(_screenshot_instance.take_screenshot(session_id=self.session_id).value)

    def __repr__(self):
        _c = dict(id=self.id, selected=self.selected, enabled=self.enabled,
                  displayed=self.displayed, position=self.position, size=self.size,
                  tag_name=self.tag_name, text=self.text)
        return repr(_c)
