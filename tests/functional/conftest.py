import pytest


from asyncio import get_event_loop_policy
from time import sleep

from .container import SelenoidDriverContainer
from .config import settings


# https://github.com/pytest-dev/pytest-asyncio/issues/171
@pytest.fixture(scope="session")
def event_loop():
    loop = get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
def firefox_client():
    with SelenoidDriverContainer(capabilities=settings.Firefox.CAPABILITIES) as container:
        yield container.get_driver()

    sleep(1)


@pytest.fixture(scope='session')
def chrome_client():
    with SelenoidDriverContainer(capabilities=settings.Chrome.CAPABILITIES) as container:
        yield container.get_driver()

    sleep(1)
