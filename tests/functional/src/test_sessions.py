class TestSession:

    def test_session(self, firefox_client):
        # get session_id
        assert len(firefox_client.sessions.id) > 0
        # get session status ready
        assert firefox_client.sessions.status.ready == True
