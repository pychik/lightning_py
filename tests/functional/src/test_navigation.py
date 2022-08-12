class TestNavi:
    def test_back_forward_title(self, selenoid_client):
        assert selenoid_client.navigation.navigate('http://google.com').navigate('https://pychik.github.io/TestPage/') \
                   .back().get_title() == "Google"
        assert selenoid_client.navigation.forward().get_title() == "Py_lightning test page"