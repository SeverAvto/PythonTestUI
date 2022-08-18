# noinspection PyUnresolvedReferences
import pytest

# noinspection PyUnresolvedReferences
from src.fixtures import steps

import time


def test_donation_button(steps):
    steps.main_page.open_donate_page()
    steps.donate_page.check_donate_page_is_open()


@pytest.mark.parametrize("search_text", ["hello", "bye", "world"])
def test_search_input(steps, search_text):
    steps.main_page.search(search_text=search_text)
    steps.main_page.check_search_result(search_text=search_text)


def test_psf_nav(steps):
    steps.main_page.psf_landing_open()
    steps.psf_landing_page.psf_about_open()
    steps.psf_about_page.check_psf_about_page_is_open()


def test_docs_nav(steps):
    steps.main_page.docs_open()
    steps.docs_page.check_docs_page_is_open()
    steps.docs_page.check_tutorial()
    steps.tutorial_page.check_tutorial_page_is_open()


def test_docs_search_input(steps):
    steps.main_page.docs_nav_bottom()
    steps.doc_page.docs_page_open()
    steps.docs_page.docs_search(search_text="Python/C API")
    steps.main_page.check_search_result(search_text="Python/C API")


def test_community_nav(steps):
    steps.main_page.community_landing_open()
    steps.community_landing_page.check_community_landing_page_is_open()


#Jobs_page_tests
def test_jobs_page_open(steps):
    steps.main_page.jobs_page_open()
    steps.jobs_page.check_jobs_page_is_open()

def test_types_button(steps):
    steps.main_page.jobs_page_open()
    steps.jobs_page.check_types_button()
    steps.jobs_page.check_types_button_is_opne_new_page()

def test_categories_button(steps):
    steps.main_page.jobs_page_open()
    steps.jobs_page.check_categories_button()
    steps.jobs_page.check_categories_page_is_open()

def test_locations_button(steps):
    steps.main_page.jobs_page_open()
    steps.jobs_page.check_locations_button()
    steps.jobs_page.check_locations_page_is_open()

def test_submit_button(steps):
    steps.main_page.jobs_page_open()
    steps.jobs_page.check_submit_button()
    steps.jobs_page.check_submit_page_is_open()

def test_sing_in_button(steps):
    steps.main_page.jobs_page_open()
    steps.jobs_page.check_sign_in_button()
    steps.jobs_page.check_submit_page_is_open()

