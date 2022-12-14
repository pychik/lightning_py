from pydantic import BaseSettings


class TestSetting(BaseSettings):
    IMAGES = {
        "firefox": "browsers/firefox:103.0",
        "chrome": "browsers/chrome:104.0",
        "edge": "browsers/edge:104.0",
        "opera": "browsers/opera:89.0",
        "safari": "browsers/safari:15.0"
    }

    class Firefox:
        CAPABILITIES = {'browserName': 'firefox', 'selenoid:options': {"enableVnc": True, "enableVideo": False}}
        # CAPABILITIES = Capabilities(browser_name='firefox', selenoidoptions={"enableVnc": True, "enableVideo": False})

    class Chrome:
        CAPABILITIES = {'browserName': 'chrome', 'selenoid:options': {"enableVnc": True, "enableVideo": False}}

    class TestPages:
        PROMPTS_TEST_PAGE: str = "https://testpages.herokuapp.com/styled/alerts/alert-test.html"


settings = TestSetting()
