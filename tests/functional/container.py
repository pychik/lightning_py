import urllib3

from lightning import Capabilities
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_container_is_ready
from .config import settings


class SelenoidDriverContainer(DockerContainer):
    def __init__(self, capabilities: Capabilities, **kwargs):
        self.capabilities = capabilities
        self.image = self._get_image_name(capabilities)
        self.port_to_expose = 4444
        self.vnc_port_to_expose = 5900
        super(SelenoidDriverContainer, self).__init__(image=self.image, **kwargs)
        self.with_exposed_ports(self.port_to_expose, self.vnc_port_to_expose)

    @staticmethod
    def _get_image_name(capabilities):
        return settings.IMAGES[capabilities['browserName']]

    @wait_container_is_ready(urllib3.exceptions.HTTPError)
    def _connect(self):
        from lightning import WebDriver
        return WebDriver(base_uri=self._get_uri(), capabilities=self.capabilities)

    def _get_uri(self):
        ip = self.get_container_host_ip()
        port = self.get_exposed_port(self.port_to_expose)
        return f"http://{ip}:{port}/wd/hub"

    def get_driver(self):
        return self._connect()
