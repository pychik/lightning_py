from __future__ import annotations

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
