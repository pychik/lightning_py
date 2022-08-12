class TestSimple:

    def test_session(self, selenoid_client):
        # get session_id
        assert len(selenoid_client.sessions.id) > 10
        # get session status ready
        assert selenoid_client.sessions.status.ready == True

