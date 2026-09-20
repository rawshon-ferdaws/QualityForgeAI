import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert products_page.get_page_title() == "Products"


@pytest.mark.regression
def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.login(
        "wrong_user",
        "wrong_password"
    )

    assert (
        "Username and password do not match"
        in login_page.get_error_message()
    )
