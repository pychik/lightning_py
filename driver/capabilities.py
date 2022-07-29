from __future__ import annotations

# import logging as log
# from swagger_client.models.capabilities import Capabilities
# from swagger_client.models.proxy import Proxy
# from swagger_client.models.timeouts import Timeouts
# from swagger_client.models.logging_prefs import LoggingPrefs
# from swagger_client.models.chrome_options import ChromeOptions
# from swagger_client.models.moon_options import MoonOptions
# from swagger_client.models.firefox_options import FirefoxOptions
# from swagger_client.models.edge_options import EdgeOptions
# from swagger_client.models.opera_options import OperaOptions
# from swagger_client.models.selenoid_options import SelenoidOptions
#
# from typing import Optional

from .exceptions import CapsException

class Capabilities(dict):
    attribute_map = {
        'browser_name': 'browserName',
        'browser_version': 'browserVersion',
        'platform_name': 'platformName',
        'accept_insecure_certs': 'acceptInsecureCerts',
        'page_load_strategy': 'pageLoadStrategy',
        'proxy': 'proxy',
        'set_window_rect': 'setWindowRect',
        'timeouts': 'timeouts',
        'strict_file_interactability': 'strictFileInteractability',
        'unhandled_prompt_behavior': 'unhandledPromptBehavior',
        'googlogging_prefs': 'goog:loggingPrefs',
        'googchrome_options': 'goog:chromeOptions',
        'moonoptions': 'moon:options',
        'mozfirefox_options': 'moz:firefoxOptions',
        'msedge_options': 'ms:edgeOptions',
        'opera_options': 'operaOptions',
        'selenoidoptions': 'selenoid:options',
        'safariautomatic_inspection': 'safari:automaticInspection',
        'safariautomatic_profiling': 'safari:automaticProfiling',
    }

    def __init__(self,  *args, **kwargs):

        # adding positional arguments to kwargs if user chooses a dict type of settings
        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise CapsException(
                        "Invalid positional arguments=%s passed to %s. "
                        "Use Dictionary {\'browserName\'=\'firefox\',...}" % (
                            args,
                            self.__class__.__name__,
                        ),
                    )

        # converting to W3c readable settings
        for var_name, var_value in kwargs.items():
            if var_name in self.attribute_map:
                self[self.attribute_map.get(var_name)] = var_value

