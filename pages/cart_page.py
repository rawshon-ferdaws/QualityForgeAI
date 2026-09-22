from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):

    # -------------------------
    # Locators
    # -------------------------

    PAGE_TITLE = (
        By.CSS_SELECTOR,
        "[data-test='title']"
    )

    CART_ITEMS = (
        By.CLASS_NAME,
        "cart_item"
    )

    ITEM_NAME = (
        By.CSS_SELECTOR,
        "[data-test='inventory-item-name']"
    )

    ITEM_PRICE = (
        By.CSS_SELECTOR,
        "[data-test='inventory-item-price']"
    )

    REMOVE_BACKPACK_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test='remove-sauce-labs-backpack']"
    )

    CONTINUE_SHOPPING_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test='continue-shopping']"
    )

    CHECKOUT_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test='checkout']"
    )

    # -------------------------
    # Page Validation
    # -------------------------

    def get_page_title(self):
        return self.get_text(
            self.PAGE_TITLE
        )

    def is_cart_page_displayed(self):
        return (
            self.get_page_title()
            == "Your Cart"
        )

    # -------------------------
    # Cart Item Information
    # -------------------------

    def wait_for_cart_item(self):
        self.wait.until(
            EC.presence_of_element_located(
                self.CART_ITEMS
            )
        )

    def get_cart_item_count(self):
        return len(
            self.driver.find_elements(
                *self.CART_ITEMS
            )
        )

    def get_item_name(self):
        return self.get_text(
            self.ITEM_NAME
        )

    def get_item_price(self):
        return self.get_text(
            self.ITEM_PRICE
        )

    # -------------------------
    # Cart Actions
    # -------------------------

    def remove_backpack(self):
        remove_button = self.wait.until(
            lambda driver: driver.find_element(
                *self.REMOVE_BACKPACK_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            remove_button
        )

    def wait_until_cart_is_empty(self):
        self.wait.until(
            lambda driver: len(
                driver.find_elements(
                    *self.CART_ITEMS
                )
            ) == 0
        )

    def continue_shopping(self):
        self.click(
            self.CONTINUE_SHOPPING_BUTTON
        )

    def checkout(self):
        checkout_button = self.wait.until(
            lambda driver: driver.find_element(
                *self.CHECKOUT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            checkout_button
        )
