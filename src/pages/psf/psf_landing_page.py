from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

from src.pages.base_page import BasePage


class PsfLandingPage(BasePage):

    @property
    def about_psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/psf/about/"]')

    @property
    def vendor_info_psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/psf/accounts-payable"]')

    @property
    def legal_psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/about/legal/"]')

    @property
    def grants_psf_nav(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@href="/psf/grants/"]')

    @property
    def grants_drop_menu_item(self) -> WebElement:
        return self.driver.find_element(By.XPATH, f'//*[@id="grants"]//*[text()="Grants Program FAQ"]')
        # return self.driver.find_element(By.XPATH, f'//a[@href="/psf/grants/faq/"]')

    # todo не могу задать переменную text, возможно потому что Леша поменял архитектуру в проекте  у себя, а я еще нет
    # @property
    # def grants_drop_menu_item(self, text) -> WebElement:
    #     return self.driver.find_element(By.XPATH, f'//*[@id="grants"]//*[text()="{ text }"]')

    # todo открыть дроп бар и оставить в наведении
    def open_grants_drop_bar(self):
        ActionChains(self.driver).move_to_element(self.grants_psf_nav).perform()


