from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utilities.config_reader import ConfigReader
from utilities.data_reader import DataReader


users = DataReader.load_json("users.json")


def login(driver):

    login_page = LoginPage(driver)

    login_page.open(
        ConfigReader.get_base_url()
    )

    user = users["valid_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    return ProductsPage(driver)


def test_products_page_displayed(driver):

    products_page = login(driver)

    assert products_page.is_products_page_displayed()
    assert products_page.get_product_count() > 0


def test_add_product_to_cart(driver):

    products_page = login(driver)

    products_page.add_backpack_to_cart()

    assert products_page.get_cart_count() == "1"


def test_remove_product_from_cart(driver):

    products_page = login(driver)

    products_page.add_backpack_to_cart()

    assert products_page.get_cart_count() == "1"

    products_page.remove_backpack_from_cart()

    assert not products_page.is_cart_badge_present()
