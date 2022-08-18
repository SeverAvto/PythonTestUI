from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.pages.base_page import BasePage

class JobsPage(BasePage):

    @property
    def sign_in_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH,"//li[@class='tier-1 last']/a[@href='/accounts/login/']")

    @property
    def jobs_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//li[@class='tier-1 element-1 current_item selected']/a[@href='/jobs/']")

    @property
    def types_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//li[@class='tier-1 element-2 ']/a[@href='/jobs/types/']")

    @property
    def menu(self) -> WebElement:
        return self.driver.find_element(By.XPATH,"//h2[@class='welcome-message']")

    @property
    def categories_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH,"//li[@class='tier-1 element-3 ']/a[@href='/jobs/categories/']")

    @property
    def locations_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//li[@class='tier-1 element-4 ']/a[@href='/jobs/locations/']")

    @property
    def submit_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//li[@class='tier-1 element-5 last']/a[@href='/jobs/create/']")

    @property
    def submit_move_sign(self) -> WebElement:
        return self.driver.find_element(By.XPATH,"//section[@class='main-content with-right-sidebar']/h1")




