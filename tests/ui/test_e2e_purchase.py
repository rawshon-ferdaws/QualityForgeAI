from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utilities.config_reader import ConfigReader
from utilities.data_reader import DataReader


users = DataReader.load_json("users.json")


def test_complete_purchase_flow(driver):

    # 1. LOGIN
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

    # 2. PRODUCTS
    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()

    assert products_page.get_cart_count() == "1"

    products_page.open_cart()

    # 3. CART
    cart_page = CartPage(driver)

    cart_page.wait_for_cart_item()

    assert cart_page.get_cart_item_count() == 1

    assert (
        cart_page.get_item_name()
        == "Sauce Labs Backpack"
    )

    cart_page.checkout()

    # 4. CHECKOUT INFORMATION
    checkout_page = CheckoutPage(driver)

    assert (
        checkout_page.get_page_title()
        == "Checkout: Your Information"
    )

    checkout_page.enter_customer_information(
        "Rawshon",
        "Ferdaws",
        "94040"
    )

    checkout_page.continue_checkout()

    checkout_page.wait_for_checkout_overview()

    # 5. CHECKOUT OVERVIEW
    assert (
        checkout_page.get_page_title()
        == "Checkout: Overview"
    )

    assert (
        checkout_page.get_item_name()
        == "Sauce Labs Backpack"
    )

    assert checkout_page.get_item_price() == "$29.99"

    # 6. COMPLETE ORDER
    checkout_page.finish_checkout()

    confirmation_message = (
        checkout_page.get_confirmation_message()
    )

    assert (
        confirmation_message
        == "Thank you for your order!"
    )
