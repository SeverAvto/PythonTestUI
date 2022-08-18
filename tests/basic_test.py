import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from src.steps import Steps


@pytest.mark.usefixtures("init_test_suite")
class BasicTest:
    steps_inst: Steps
    driver_inst: WebDriver

    @property
    def steps(self) -> Steps:
        return self.steps_inst

    @property
    def driver(self) -> WebDriver:
        return self.driver_inst
