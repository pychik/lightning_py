from pydantic import BaseSettings


class TestSetting(BaseSettings):
    CAPABILITIES = {'browser_name': 'firefox', 'selenoidoptions': {"enableVnc": True, "enableVideo": False}}
    TEST_CAPS: dict = {
        "browserName": "firefox",
        "acceptInsecureCerts": True,
        "moz:debuggerAddress": True,
        }


settings = TestSetting()
