from pydantic import BaseSettings


class TestSetting(BaseSettings):
    CAPABILITIES_FF = {'browserName': 'firefox', 'selenoid:options': {"enableVnc": True, "enableVideo": False}}
    # CAPABILITIES = Capabilities(browser_name='firefox', selenoidoptions={"enableVnc": True, "enableVideo": False})
    TEST_CAPS_FF: dict = {
        "browserName": "firefox",
        "acceptInsecureCerts": True,
        "moz:debuggerAddress": True,
        }


settings = TestSetting()
