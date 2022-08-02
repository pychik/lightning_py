import pytest
from tests.functional.settings import TestSetting
from testcontainers.selenium import BrowserWebDriverContainer
from testcontainers.core.waiting_utils import wait_container_is_ready
from time import sleep
import urllib3
from driver import WebDriver


@pytest.fixture(scope='session')
def settings() -> TestSetting:
    return TestSetting()


@pytest.fixture(scope='session')
def selenoid_container(settings):
    with BrowserWebDriverContainer(settings.test_caps) as firefox:
        yield firefox


@pytest.fixture(scope='session')
def selenoid_client(settings):
    firefox = BrowserWebDriverContainer(settings.TEST_CAPS)
    firefox.start()

    @wait_container_is_ready(urllib3.exceptions.HTTPError)
    def connect():
        base_uri = firefox.get_connection_url()
        print("BASE_URI", base_uri)
        client = WebDriver(base_uri=base_uri)
        return client
    c = connect()
    yield c
    c.close()
    sleep(1)
    firefox.stop()
