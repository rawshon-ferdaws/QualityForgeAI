import pytest

from selenium import webdriver

from api.clients import APIClient
from utilities.config_reader import ConfigReader


@pytest.fixture
def driver():
    browser = ConfigReader.get_browser()

    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()

        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-backgrounding-occluded-windows")
        options.add_argument("--disable-renderer-backgrounding")

        driver = webdriver.Chrome(
            options=options
        )

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()

    else:
        raise ValueError(
            f"Unsupported browser: {browser}"
        )

    yield driver

    driver.quit()


@pytest.fixture
def api_client():
    return APIClient()
