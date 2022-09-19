from __future__ import annotations

from lightning_adapter.api.elements_api import ElementsApi
from lightning_adapter.models.find_element_response_value import FindElementResponseValue
from lightning_adapter.models.find_element_request import FindElementRequest

from .exceptions import ELEMENTS_ERROR, webdriver_exception
from .mixin import Common
from .webelement import Locator, WebElement


class Elements(Common):
    def __init__(self, wd):
        super().__init__(wd)
        self._elements_instance = ElementsApi(self._api_client)

    @property
    @webdriver_exception(ELEMENTS_ERROR)
    def current(self) -> WebElement:
        _response = self._elements_instance.get_active_element(session_id=self.session_id).value
        _web_element = WebElement(elements_instance=self._elements_instance,
                                  id=_response.element_6066_11e4_a52e_4f735466cecf,
                                  session_id=self.session_id)
        return _web_element

    @webdriver_exception(ELEMENTS_ERROR)
    def find_all(self, locator: Locator) -> list[WebElement]:
        _body = FindElementRequest(using=locator.strategy, value=locator.expression)
        _response: list[FindElementResponseValue] = self._elements_instance.find_elements(session_id=self.session_id,
                                                                                          body=_body).value

        _web_elements = list(map(lambda e: WebElement(elements_instance=self._elements_instance,
                                                      id=e.element_6066_11e4_a52e_4f735466cecf,
                                                      session_id=self.session_id), _response))
        return _web_elements

    @webdriver_exception(ELEMENTS_ERROR)
    def find_first(self, locator: Locator) -> WebElement:
        _body = FindElementRequest(using=locator.strategy, value=locator.expression)
        _response: FindElementResponseValue = self._elements_instance.find_element(session_id=self.session_id,
                                                                                   body=_body).value
        _web_element = WebElement(elements_instance=self._elements_instance,
                                  id=_response.element_6066_11e4_a52e_4f735466cecf,
                                  session_id=self.session_id)
        return _web_element
