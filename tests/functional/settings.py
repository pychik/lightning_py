from pydantic import BaseSettings


class TestSetting(BaseSettings):
    TEST_CAPS: dict = {
        "browserName": "firefox",
        "acceptInsecureCerts": True,
        "moz:debuggerAddress": True,
        }


settings = TestSetting()
