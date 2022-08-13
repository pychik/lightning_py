class TestSimple:

    def test_session(self, firefox_client):
        # get session_id
        assert len(firefox_client.sessions.id) > 10
        # get session status ready
        assert firefox_client.sessions.status.ready == True

