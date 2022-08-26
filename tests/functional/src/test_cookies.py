class TestCookies:
    def test_all_add_get_delete(self, firefox_client):
        r = firefox_client.navigation.navigate('https://pychik.github.io/lightning_py/pages/1').cookies.all
        assert r == []
        from lightning import Cookie
        test_cookie = Cookie(name="TestNameCookie", value="TestValueCookie")

        firefox_client.cookies.add(cookie=test_cookie)
        assert len(firefox_client.cookies.all) > 0
        del firefox_client.cookies.all
        assert len(firefox_client.cookies.all) == 0

        firefox_client.cookies.add(cookie=test_cookie)
        assert firefox_client.cookies.get(name=test_cookie.name).name == test_cookie.name
        assert len(firefox_client.cookies.all) > 0
        firefox_client.cookies.delete(name=test_cookie.name)
        assert len(firefox_client.cookies.all) == 0
