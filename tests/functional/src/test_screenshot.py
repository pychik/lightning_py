class TestScreenshot:

    def test_screenshot(self, firefox_client):
        screenshot = firefox_client.navigation.navigate('http://google.com').screenshot.take()
        assert isinstance(screenshot, bytes)
        assert len(screenshot) > 50
