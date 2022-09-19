from pytest import raises

from lightning.webelement import By


class TestElements:
    def test_find_first_missing_element(self, firefox_client):

        from lightning.exceptions import WebDriverException

        with raises(WebDriverException):
            firefox_client.navigation.navigate("https://example.com/")\
                          .elements.find_first(locator=By.css_selector("missing-element"))

    def test_find_first_css_selector(self, firefox_client):
        web_element = firefox_client.navigation.navigate("https://example.com/") \
            .elements.find_first(locator=By.css_selector("div h1"))
        assert len(web_element.text) > 0

    def test_find_first_tag_name(self, firefox_client):

        web_element = firefox_client.navigation.navigate("https://example.com/")\
                           .elements.find_first(locator=By.tag_name("h1"))
        assert len(web_element.text) > 0

    def test_find_first_xpath(self, firefox_client):
        web_element = firefox_client.navigation.navigate("https://example.com/") \
            .elements.find_first(locator=By.xpath("/html/body/div/h1"))
        assert len(web_element.text) > 0

    def test_find_first_link_text(self, firefox_client):
        web_element = firefox_client.navigation.navigate("https://example.com/") \
            .elements.find_first(locator=By.link_text("More information..."))

        assert len(web_element.text) > 0

    def test_find_first_partial_link_text(self, firefox_client):
        web_element = firefox_client.navigation.navigate("https://example.com/") \
            .elements.find_first(locator=By.partial_link_text("More"))
        assert len(web_element.text) > 0

    def test_find_all_missing_element(self, firefox_client):
        web_elements = firefox_client.navigation.navigate("https://example.com/")\
                          .elements.find_all(locator=By.css_selector("missing-element"))
        assert len(web_elements) == 0

    def test_find_all_tag_name(self, firefox_client):
        web_elements = firefox_client.navigation.navigate("https://example.com/")\
                          .elements.find_all(locator=By.tag_name("h1"))
        assert len(web_elements) > 0

    def test_active_element(self, firefox_client):
        active_element = firefox_client.navigation.navigate("https://example.com/").elements.current
        assert len(active_element.id) > 0

    def test_web_element_find_first(self, firefox_client):
        body_element = firefox_client.navigation.navigate("https://example.com/")\
                           .elements.find_first(locator=By.tag_name("body"))
        h1_nested_element = body_element.find_first(locator=By.tag_name("h1"))
        assert len(h1_nested_element.text) > 0

    def test_web_element_find_all(self, firefox_client):
        body_element = firefox_client.navigation.navigate("https://example.com/")\
                                     .elements.find_first(locator=By.tag_name("body"))
        nested_elements = body_element.find_all(locator=By.tag_name("h1"))
        assert len(nested_elements) == 1

    def test_web_element_methods(self, firefox_client):
        href_element = firefox_client.navigation.navigate("https://example.com/")\
                                     .elements.find_first(locator=By.css_selector("a[href]"))
        assert href_element.tag_name == "a"

        from lightning.window import Position, Size
        element_position = href_element.position
        element_size = href_element.size
        assert isinstance(element_position, Position) and element_position.x > 0 and element_position.y > 0
        assert isinstance(element_size, Size) and element_size.width > 0 and element_size.height > 0

        check_href = href_element.attribute(name="href")
        assert isinstance(check_href, str) and len(check_href) > 0

        check_missing_attribute = href_element.attribute(name="missing_attribute")
        assert check_missing_attribute is None

        assert href_element.selected is False
        assert href_element.enabled is True
        assert href_element.displayed is True

        element_css_property = href_element.css_property("font-family")
        assert isinstance(element_css_property, str) and len(element_css_property) > 0
        missing_element_css_property = href_element.css_property("missing-property")
        assert isinstance(missing_element_css_property, str) and len(missing_element_css_property) == 0

        current_url = firefox_client.navigation.current_url
        href_element.click()
        new_url = firefox_client.navigation.current_url
        assert current_url != new_url

    def test_send_keys(self, firefox_client):
        input_element = firefox_client.navigation.navigate("https://www.w3schools.com/html/html_forms.asp") \
                                                 .elements.find_first(locator=By.css_selector("input#fname"))
        input_property = input_element.element_property("value")
        assert isinstance(input_property, str) and len(input_property) > 0
        input_element.clear()
        input_property = input_element.element_property("value")
        assert isinstance(input_property, str) and len(input_property) == 0
        input_element.send_keys(text="some text")
        input_property = input_element.element_property("value")
        assert input_property == "some text"

    def test_accessibilities(self, chrome_client):
        # using chrome_client because firefox doesn't support get_computed_methods

        href_element = chrome_client.navigation.navigate("https://example.com/")\
                                     .elements.find_first(locator=By.css_selector("a[href]"))
        element_role = href_element.accessibility().role
        element_label = href_element.accessibility().label
        assert element_role == "link"
        assert isinstance(element_label, str) and len(element_label) > 0
