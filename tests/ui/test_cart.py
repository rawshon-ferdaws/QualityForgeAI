from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

from utilities.config_reader import ConfigReader
from utilities.data_reader import DataReader


users = DataReader.load_json("users.json")


def open_cart_with_product(driver):

    login_page = LoginPage(driver)

    login_page.open(
        ConfigReader.get_base_url()
    )

    user = users["valid_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()

    # Verify product was actually added
    assert products_page.get_cart_count() == "1"

    products_page.open_cart()

    cart_page = CartPage(driver)

    # Wait until cart item is loaded
    cart_page.wait_for_cart_item()

    return cart_page


# 1. Verify cart page
def test_cart_page_displayed(driver):

    cart_page = open_cart_with_product(driver)

    assert cart_page.is_cart_page_displayed()


# 2. Verify product was added to cart
def test_product_in_cart(driver):

    cart_page = open_cart_with_product(driver)

    assert cart_page.get_cart_item_count() == 1

    assert (
        cart_page.get_item_name()
        == "Sauce Labs Backpack"
    )


# 3. Verify product price
def test_product_price_in_cart(driver):

    cart_page = open_cart_with_product(driver)

    assert cart_page.get_item_price() == "$29.99"


# 4. Remove product from cart
def test_remove_product_from_cart(driver):

    cart_page = open_cart_with_product(driver)

    assert cart_page.get_cart_item_count() == 1

    cart_page.remove_backpack()

    cart_page.wait_until_cart_is_empty()

    assert cart_page.get_cart_item_count() == 0
