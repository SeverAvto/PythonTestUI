import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.steps import Steps


@pytest.yield_fixture()
def steps() -> Steps:
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(
            path="/Users/romanovaleks/PycharmProjects/TestUI-ivanrussui"
        ).install()),
        # options=None,
    )

    driver.get("http://www.python.org")

    steps_obj = Steps(driver)

    yield steps_obj

    driver.quit()
