from ..config import settings


class TestPrompts:
    def test_accept(self, firefox_client):
        from lightning.webelement import By
        firefox_client.navigation.navigate(settings.TestPages.PROMPTS_TEST_PAGE)\
                      .elements.find_first(By.css_selector("#alertexamples")).click()

        text = firefox_client.prompts.text
        assert len(text) > 0
        firefox_client.prompts.accept()

    def test_dismiss(self, firefox_client):
        from lightning.webelement import By
        firefox_client.navigation.navigate(settings.TestPages.PROMPTS_TEST_PAGE) \
                      .elements.find_first(By.css_selector("#confirmexample")).click()
        firefox_client.prompts.dismiss()

    def test_send_keys(self, firefox_client):
        from lightning.webelement import By
        firefox_client.navigation.navigate(settings.TestPages.PROMPTS_TEST_PAGE) \
            .elements.find_first(By.css_selector("#promptexample")).click()
        firefox_client.prompts.text = "some-text"
