import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.mark.smoke
@pytest.mark.regression
def test_add_product_to_cart(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page.add_backpack_to_cart()

    assert products_page.get_cart_count() == "1"


@pytest.mark.regression
def test_remove_product_from_products_page(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page.add_backpack_to_cart()
    products_page.remove_backpack_from_cart()

    assert products_page.is_visible(
        products_page.ADD_BACKPACK_BUTTON
    )
