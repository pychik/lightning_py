class TestSimple:
    def test_get(self, selenoid_client):
        assert len(selenoid_client.session_id) > 10
        response = selenoid_client.navigation.navigate('http://google.com').document.get_page_source()
        assert response.startswith("<html")

    # not necessary test
    def test_back_forward_title(self, selenoid_client):
        assert selenoid_client.navigation.navigate('http://google.com').navigate('https://pychik.github.io/TestPage/')\
                   .back().get_title() == "Google"
        assert selenoid_client.navigation.forward().get_title() == "Py_lightning test page"

    def test_screenshot(self, selenoid_client):
        assert len(selenoid_client.navigation.navigate('http://google.com').screenshot.take()) > 50
