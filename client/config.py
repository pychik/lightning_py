from .capabilities import Capabilities


class Defaults:
    BASE_URI = 'http://localhost:4444/wd/hub'
    CAPABILITIES = Capabilities(browser_name='firefox', selenoidoptions={"enableVnc": True, "enableVideo": False})
    CAPABILITIES_NO_VNC = {
                            "browserName": "firefox",
                            "browserVersion": "101.0",
                          }
