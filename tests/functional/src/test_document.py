class TestDocument:
    def test_document(self, firefox_client):
        response = firefox_client.navigation.navigate('http://google.com').document.get_page_source()
        assert response.startswith("<html")
