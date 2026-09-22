from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader
from utilities.data_reader import DataReader


users = DataReader.load_json("users.json")


def test_valid_login(driver):

    login_page = LoginPage(driver)

    login_page.open(
        ConfigReader.get_base_url()
    )

    user = users["valid_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    assert "inventory.html" in driver.current_url


def test_invalid_login(driver):

    login_page = LoginPage(driver)

    login_page.open(
        ConfigReader.get_base_url()
    )

    user = users["invalid_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    error_message = login_page.get_error_message()

    assert "Username and password do not match" in error_message


def test_locked_out_user(driver):

    login_page = LoginPage(driver)

    login_page.open(
        ConfigReader.get_base_url()
    )

    user = users["locked_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    error_message = login_page.get_error_message()

    assert "locked out" in error_message.lower()
