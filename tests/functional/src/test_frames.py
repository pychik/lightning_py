class TestFrames:

    def test_frames(self, firefox_client):
        from lightning.webelement import By
        element_frame = firefox_client.navigation\
                                      .navigate("https://www.w3.org/WAI/UA/TS/html401/cp0101/0101-FRAME-TEST.html") \
                                      .elements.find_first(By.css_selector("frame[name='target2']"))

        firefox_client.frames.switch_to(element=element_frame)
        firefox_client.frames.switch_to_parent()
        firefox_client.frames.switch_to(index=1)
        firefox_client.frames.switch_to_default()
