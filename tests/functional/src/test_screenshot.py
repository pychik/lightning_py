class TestScreenshot:

    def test_screenshot(self, selenoid_client):
        screenshot = selenoid_client.navigation.navigate('http://google.com').screenshot.take()
        assert isinstance(screenshot, bytes)
        assert len(screenshot) > 50
