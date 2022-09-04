class TestWindows:
    def test_windows(self, firefox_client):
        windows_list = firefox_client.windows.list()
        assert len(windows_list) == 1
        firefox_client.windows.create_window()
        windows_list = firefox_client.windows.list()
        assert len(windows_list) == 2
        firefox_client.windows.create_tab()
        assert len(windows_list) == 2

        current_window = firefox_client.windows.current()
        from lightning import Size, Position, Window
        assert isinstance(current_window, Window)
        assert isinstance(current_window.size, Size)
        assert isinstance(current_window.position, Position)

    def test_window(self, firefox_client):
        window_init = firefox_client.navigation.navigate('https://pychik.github.io/lightning_py/pages/1')\
                                    .windows.current()
        window_1 = firefox_client.windows.create_window()
        tab_1 = firefox_client.windows.create_tab()
        assert window_init.handle != window_1.handle != tab_1.handle

        window_init.switch_to()
        title_window_init = firefox_client.navigation.get_title
        window_1.switch_to()
        title_window_1 = firefox_client.navigation.navigate('https://pychik.github.io/lightning_py/pages/2')\
                                                  .get_title
        assert title_window_init != title_window_1

        assert window_init.position != window_1.position

        size_window_1 = window_1.size
        assert window_1.minimize().maximize().fullscreen().size != size_window_1

        from lightning import Size, Position
        window_1.size = Size(width=800, height=600)
        window_1.position = Position(x=1, y=4)
        check_window_1 = firefox_client.windows.current()
        assert check_window_1.size.width == window_1.size.width, check_window_1.size.height == window_1.size.height
        assert check_window_1.position.x == window_1.position.x, check_window_1.position.y == window_1.position.y
