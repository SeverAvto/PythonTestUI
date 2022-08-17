from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.pages.base_page import BasePage


class PsfLandingPage(BasePage):

    @property
    def about_psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/psf/about/"]')

    @property
    def grants_psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/psf/grants/"]')

    @property
    def vendor_info_psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/psf/accounts-payable"]')
