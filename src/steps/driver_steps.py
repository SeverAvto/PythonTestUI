import os.path

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class DriverSteps:

    @property
    def driver_path(self):
        return "/Users/romanovaleks/PycharmProjects/TestUI-ivanrussui/lib/chromedriver"

    def create_driver_and_open_python_page(self) -> WebDriver:
        driver = webdriver.Chrome(executable_path=self.driver_path)
        driver.get("https://www.python.org/")
        return driver
