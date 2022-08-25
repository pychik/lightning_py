class TestDocument:
    def test_page_source(self, firefox_client):
        response = firefox_client.navigation.navigate('https://pychik.github.io/lightning_py/pages/1')\
                                            .document.page_source
        assert response.startswith("<html")

    def test_execute_script(self, firefox_client):
        res = firefox_client.document.execute_script("return arguments[0] + arguments[1];", 1, 2)
        assert res == 3
        res = firefox_client.document.execute_script("return arguments[0] + arguments[1];", "1", "2")
        assert res == "12"

    def test_execute_async_script(self, firefox_client):
        r = firefox_client.document.execute_async_script("var x = arguments[0]; var y = arguments[1];"
                                                         "var result = x + y; "
                                                         "callback = arguments[arguments.length - 1];"
                                                         "window.setTimeout(callback(result), 100);",
                                                         40, 2)
        assert r == 42
        r = firefox_client.document.execute_async_script("var x = arguments[0]; var y = arguments[1];"
                                                         "var result = x + y; "
                                                         "callback = arguments[arguments.length - 1];"
                                                         "window.setTimeout(callback(result), 100);",
                                                         "40", "2")
        assert r == "402"
