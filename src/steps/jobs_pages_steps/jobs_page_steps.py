from src.pages.jobs_pages.jobs_page import JobsPage
from src.steps.base_steps import BaseSteps


class JobsPageSteps(BaseSteps):

    @property
    def jobs_page(self) -> JobsPage:
        return JobsPage(self.driver)

    def check_jobs_page_is_open(self):
        assert self.jobs_page.jobs_button.is_displayed(), 'No displayed'
        assert self.jobs_page.jobs_button.text == 'Jobs', 'Text is not correct'

    def check_types_button(self):
        assert self.jobs_page.types_button.is_displayed(), "No dispalyed"
        assert self.jobs_page.types_button.text == "Types", "Text is not correct"
        self.jobs_page.types_button.click()

    def check_types_button_is_opne_new_page(self):
        assert self.jobs_page.menu.is_displayed(), "No displayed"
        assert self.jobs_page.menu.text == "Jobs by Technology!", "Text is not correct"

    def check_categories_button(self):
        assert self.jobs_page.categories_button.is_displayed(), "No displayed"
        assert self.jobs_page.categories_button.text == "Categories", "Text is not correct"
        self.jobs_page.categories_button.click()

    def check_categories_page_is_open(self):
        assert self.jobs_page.menu.is_displayed(), "No displayed"
        assert self.jobs_page.menu.text == "Job Categories", "Text is not correct"

    def check_locations_button(self):
        assert self.jobs_page.locations_button.is_displayed(), "No displayed"
        assert self.jobs_page.locations_button.text == "Locations", "Text is not correct"
        self.jobs_page.locations_button.click()

    def check_locations_page_is_open(self):
        assert self.jobs_page.menu.is_displayed(), "No displayed"
        assert self.jobs_page.menu.text == "Jobs by Location!", "Text is not correct"

    def check_submit_button(self):
        assert self.jobs_page.submit_button.is_displayed(), "No displayed"
        assert self.jobs_page.submit_button.text == "Submit", "Text is not correct"
        self.jobs_page.submit_button.click()

    def check_submit_page_is_open(self):
        assert self.jobs_page.submit_move_sign.is_displayed(), "No displayed"
        assert self.jobs_page.submit_move_sign.text == "Sign In", "Text is not correct"

    def check_sign_in_button(self):
        assert self.jobs_page.sign_in_button.is_displayed(),"No displayed"
        assert self.jobs_page.sign_in_button.text == "Sign In", "Text is not correct"
        self.jobs_page.sign_in_button.click()



