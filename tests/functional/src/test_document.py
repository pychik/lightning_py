class TestDocument:
    def test_document(self, firefox_client):
        response = firefox_client.navigation.navigate('https://pychik.github.io/lightning_py/pages/1')\
                                            .document.get_page_source()
        assert response.startswith("<html")
