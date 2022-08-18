import pytest
import allure

from .basic_test import BasicTest


@allure.suite("UI тесты")
@allure.sub_suite("Главная страница Python org")
class TestMainPage(BasicTest):

    def test_donation_button(self):
        self.steps.main_page.open_donate_page()
        self.steps.donate_page.check_donate_page_is_open()

    @pytest.mark.parametrize("search_text", ["hello", "bye", "world"])
    def test_search_input(self, search_text):
        self.steps.main_page.search(search_text=search_text)
        self.steps.main_page.check_search_result(search_text=search_text)

    def test_psf_nav(self):
        self.steps.main_page.psf_landing_open()
        self.steps.psf_landing_page.psf_about_open()
        self.steps.psf_about_page.check_psf_about_page_is_open()

    def test_docs_nav(self):
        self.steps.main_page.docs_open()
        self.steps.docs_page.check_docs_page_is_open()
        self.steps.docs_page.check_tutorial()
        self.steps.tutorial_page.check_tutorial_page_is_open()

    def test_community_nav(self):
        self.steps.main_page.community_landing_open()
        self.steps.community_landing_page.check_community_landing_page_is_open()

    @allure.title("Проверка нажатия на FAQ кнопку")
    def test_test(self):
        self.steps.main_page.open_news_drop_bar_item("FAQ")
