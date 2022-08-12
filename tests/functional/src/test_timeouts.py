class TestTimeouts:

    def test_timeouts(self, selenoid_client):
        assert selenoid_client.timeouts.implicit_wait_timeout == 0
        assert selenoid_client.timeouts.page_load_timeout == 300000
        assert selenoid_client.timeouts.script_timeout == 30000
        selenoid_client.timeouts.implicit_wait_timeout = 1
        selenoid_client.timeouts.page_load_timeout = 250000
        selenoid_client.timeouts.script_timeout = 25000
        assert selenoid_client.timeouts.implicit_wait_timeout == 1
        assert selenoid_client.timeouts.page_load_timeout == 250000
        assert selenoid_client.timeouts.script_timeout == 25000
