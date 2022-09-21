class TestPrint:
    def test_print(self, firefox_client):
        from lightning.print import PrintSettings
        print_set = PrintSettings()
        print_set.width = 210.0
        print_set.height = 297.0
        print_set.scale = 0.5
        # print_set.original_size =
        print_set.margin_top = 1.5
        print_set.margin_bottom = 1.5
        print_set.margin_left = 1.5
        print_set.margin_right = 1.5
        # print_set.landscape =
        print_set.add_pages(1)
        print_set.add_pages("2-3")
        _pd_file = firefox_client.navigation.navigate("https://example.com").print.pdf(settings=print_set)

        assert len(_pd_file) > 0
