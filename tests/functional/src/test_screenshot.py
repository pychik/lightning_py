class TestScreenshot:

    def test_screenshot(self, firefox_client):
        screenshot = firefox_client.navigation.navigate('https://pychik.github.io/lightning_py/pages/1')\
                                              .screenshot.take()
        assert isinstance(screenshot, bytes)
        assert len(screenshot) > 0
