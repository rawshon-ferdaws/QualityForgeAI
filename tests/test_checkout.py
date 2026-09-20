import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.mark.smoke
@pytest.mark.regression
def test_successful_checkout(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page.add_backpack_to_cart()
    products_page.open_cart()
    cart_page.click_checkout()

    checkout_page.enter_customer_information(
        "Test",
        "User",
        "94040"
    )
    checkout_page.click_continue()
    checkout_page.click_finish()

    assert checkout_page.get_success_message() == "Thank you for your order!"


@pytest.mark.regression
def test_checkout_without_first_name(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page.add_backpack_to_cart()
    products_page.open_cart()
    cart_page.click_checkout()

    checkout_page.enter_customer_information(
        "",
        "User",
        "94040"
    )
    checkout_page.click_continue()

    assert "First Name is required" in checkout_page.get_error_message()
