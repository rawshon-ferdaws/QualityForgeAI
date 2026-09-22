from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utilities.config_reader import ConfigReader
from utilities.data_reader import DataReader


users = DataReader.load_json("users.json")


def open_checkout(driver):
    """
    Login -> Add product -> Open cart -> Checkout
    """

    # Login
    login_page = LoginPage(driver)

    login_page.open(
        ConfigReader.get_base_url()
    )

    user = users["valid_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    # Products
    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()

    assert products_page.get_cart_count() == "1"

    products_page.open_cart()

    # Cart
    cart_page = CartPage(driver)

    cart_page.wait_for_cart_item()

    assert cart_page.get_cart_item_count() == 1

    cart_page.checkout()

    # Checkout
    return CheckoutPage(driver)


def test_checkout_page_displayed(driver):
    """
    Verify Checkout: Your Information page opens.
    """

    checkout_page = open_checkout(driver)

    assert (
        checkout_page.get_page_title()
        == "Checkout: Your Information"
    )


def test_checkout_with_valid_information(driver):
    """
    Enter valid customer information
    and continue to checkout overview.
    """

    checkout_page = open_checkout(driver)

    checkout_page.enter_customer_information(
        "Rawshon",
        "Ferdaws",
        "94040"
    )

    checkout_page.continue_checkout()

    checkout_page.wait_for_checkout_overview()

    assert (
        checkout_page.get_page_title()
        == "Checkout: Overview"
    )


def test_checkout_missing_first_name(driver):
    """
    Verify validation when first name is missing.
    """

    checkout_page = open_checkout(driver)

    checkout_page.enter_customer_information(
        "",
        "Ferdaws",
        "94040"
    )

    checkout_page.continue_checkout()

    error_message = checkout_page.get_error_message()

    assert "First Name is required" in error_message


def test_checkout_missing_last_name(driver):
    """
    Verify validation when last name is missing.
    """

    checkout_page = open_checkout(driver)

    checkout_page.enter_customer_information(
        "Rawshon",
        "",
        "94040"
    )

    checkout_page.continue_checkout()

    error_message = checkout_page.get_error_message()

    assert "Last Name is required" in error_message


def test_checkout_missing_postal_code(driver):
    """
    Verify validation when postal code is missing.
    """

    checkout_page = open_checkout(driver)

    checkout_page.enter_customer_information(
        "Rawshon",
        "Ferdaws",
        ""
    )

    checkout_page.continue_checkout()

    error_message = checkout_page.get_error_message()

    assert "Postal Code is required" in error_message


def test_checkout_overview_product(driver):
    """
    Verify product information on Checkout Overview.
    """

    checkout_page = open_checkout(driver)

    checkout_page.enter_customer_information(
        "Rawshon",
        "Ferdaws",
        "94040"
    )

    checkout_page.continue_checkout()

    checkout_page.wait_for_checkout_overview()

    assert (
        checkout_page.get_item_name()
        == "Sauce Labs Backpack"
    )

    assert (
        checkout_page.get_item_price()
        == "$29.99"
    )


def test_complete_checkout(driver):
    """
    Complete the purchase and verify confirmation.
    """

    checkout_page = open_checkout(driver)

    checkout_page.enter_customer_information(
        "Rawshon",
        "Ferdaws",
        "94040"
    )

    checkout_page.continue_checkout()

    import time
    time.sleep(1)

    checkout_page.wait_for_checkout_overview()

    checkout_page.finish_checkout()

    time.sleep(1)

    confirmation_message = (
        checkout_page.get_confirmation_message()
    )

    assert (
        confirmation_message
        == "Thank you for your order!"
    )
