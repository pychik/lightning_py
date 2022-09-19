class TestNavi:
    def test_back_forward_title_refresh(self, firefox_client):
        assert firefox_client.navigation.navigate('https://pychik.github.io/lightning_py/pages/1')\
                   .navigate('https://pychik.github.io/lightning_py/pages/2') \
                   .back().get_title == "Py_lightning test page №1"
        assert firefox_client.navigation.forward().get_title == "Py_lightning test page №2"
        assert firefox_client.navigation.refresh().get_title == "Py_lightning test page №2"
