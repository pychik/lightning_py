from __future__ import annotations

from typing import Tuple, Optional
from swagger_client.api.timeouts_api import TimeoutsApi
from swagger_client.models.timeouts import Timeouts as TimeoutsModel

from .mixin import Common


class Timeouts(Common):
    def __init__(self, wd):
        super().__init__(wd)
        self._timeouts_instance = TimeoutsApi(self._api_client)
        self._timeouts: TimeoutsModel = self.timeouts

    @property
    def timeouts(self):
        self._timeouts = self._timeouts_instance.get_timeouts(session_id=self.session_id).value
        return self._timeouts

    @property
    def implicit_wait_timeout(self):
        return self._timeouts.implicit

    @implicit_wait_timeout.setter
    def implicit_wait_timeout(self, value):
        self._timeouts.implicit = value
        pass

    @property
    def page_load_timeout(self):
        return self._timeouts.page_load

    @page_load_timeout.setter
    def page_load_timeout(self, value):
        self._timeouts.page_load = value

    @property
    def script_timeout(self):
        return self._timeouts.script

    @script_timeout.setter
    def script_timeout(self, value):
        self._timeouts.script = value

    def __repr__(self):
        return str(self.timeouts)
# @property + @attribute.setter client.timeouts().implicit_wait_timeout
#  @property + @attribute.setter client.timeouts().page_load_timeout
#  @property + @attribute.setter client.timeouts().script_timeout using Optional for getter
