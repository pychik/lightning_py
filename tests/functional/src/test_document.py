class TestDocument:
    def test_document(self, selenoid_client):
        response = selenoid_client.navigation.navigate('http://google.com').document.get_page_source()
        assert response.startswith("<html")
