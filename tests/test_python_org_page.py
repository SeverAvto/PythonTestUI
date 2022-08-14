import steps


def test_donation_button():
    driver = steps.driver_steps().create_driver_and_open_python_page()
    steps.main_page(driver).open_donate_page()
    steps.donate_page(driver).check_donate_page_is_open()


def test_search_input():
    driver = steps.driver_steps().create_driver_and_open_python_page()
    steps.main_page(driver).search(search_text="hello")
    steps.main_page(driver).check_search_result(search_text="hello")


def test_psf_nav():
    driver = steps.driver_steps().create_driver_and_open_python_page()
    steps.main_page(driver).psf_landing_open()
    steps.psf_landing_page(driver).psf_about_open()
    steps.psf_about_page(driver).check_psf_about_page_is_open()


def test_docs_nav():
    driver = steps.driver_steps().create_driver_and_open_python_page()
    steps.main_page(driver).docs_open()
    steps.docs_page(driver).check_docs_page_is_open()
    steps.docs_page(driver).check_tutorial()
    steps.tutorial_page(driver).check_tutorial_page_is_open()

# def
