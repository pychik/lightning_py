class TestNavi:
    def test_back_forward_title(self, firefox_client):
        assert firefox_client.navigation.navigate('http://google.com').navigate('https://pychik.github.io/TestPage/') \
                   .back().get_title() == "Google"
        assert firefox_client.navigation.forward().get_title() == "Py_lightning test page"