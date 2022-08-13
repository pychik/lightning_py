class TestTimeouts:

    def test_timeouts(self, firefox_client):
        assert firefox_client.timeouts.implicit_wait_timeout == 0
        assert firefox_client.timeouts.page_load_timeout == 300000
        assert firefox_client.timeouts.script_timeout == 30000
        firefox_client.timeouts.implicit_wait_timeout = 1
        firefox_client.timeouts.page_load_timeout = 250000
        firefox_client.timeouts.script_timeout = 25000
        assert firefox_client.timeouts.implicit_wait_timeout == 1
        assert firefox_client.timeouts.page_load_timeout == 250000
        assert firefox_client.timeouts.script_timeout == 25000
