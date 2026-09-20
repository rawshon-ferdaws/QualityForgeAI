import pytest

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.mark.smoke
@pytest.mark.regression
def test_product_is_added_to_cart(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page.add_backpack_to_cart()
    products_page.open_cart()

    assert cart_page.get_item_name() == "Sauce Labs Backpack"


@pytest.mark.regression
def test_continue_to_checkout(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page.add_backpack_to_cart()
    products_page.open_cart()
    cart_page.click_checkout()

    assert "checkout-step-one" in driver.current_url
