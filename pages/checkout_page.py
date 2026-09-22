from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    # -------------------------
    # Customer Information
    # -------------------------

    PAGE_TITLE = (
        By.CSS_SELECTOR,
        "[data-test='title']"
    )

    FIRST_NAME = (
        By.ID,
        "first-name"
    )

    LAST_NAME = (
        By.ID,
        "last-name"
    )

    POSTAL_CODE = (
        By.ID,
        "postal-code"
    )

    CONTINUE_BUTTON = (
        By.ID,
        "continue"
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    # -------------------------
    # Checkout Overview
    # -------------------------

    ITEM_NAME = (
        By.CSS_SELECTOR,
        "[data-test='inventory-item-name']"
    )

    ITEM_PRICE = (
        By.CSS_SELECTOR,
        "[data-test='inventory-item-price']"
    )

    ITEM_TOTAL = (
        By.CSS_SELECTOR,
        "[data-test='subtotal-label']"
    )

    TAX = (
        By.CSS_SELECTOR,
        "[data-test='tax-label']"
    )

    TOTAL = (
        By.CSS_SELECTOR,
        "[data-test='total-label']"
    )

    FINISH_BUTTON = (
        By.ID,
        "finish"
    )

    CANCEL_BUTTON = (
        By.ID,
        "cancel"
    )

    # -------------------------
    # Checkout Complete
    # -------------------------

    COMPLETE_HEADER = (
        By.CSS_SELECTOR,
        "[data-test='complete-header']"
    )

    COMPLETE_TEXT = (
        By.CSS_SELECTOR,
        "[data-test='complete-text']"
    )

    BACK_HOME_BUTTON = (
        By.ID,
        "back-to-products"
    )

    # -------------------------
    # Actions
    # -------------------------

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def enter_first_name(self, first_name):
        self.type(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.type(self.LAST_NAME, last_name)

    def enter_postal_code(self, postal_code):
        self.type(self.POSTAL_CODE, postal_code)

    def enter_customer_information(
        self,
        first_name,
        last_name,
        postal_code
    ):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def continue_checkout(self):
        continue_button = self.wait.until(
            lambda driver: driver.find_element(
                *self.CONTINUE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            continue_button
        )

    def wait_for_checkout_overview(self):
        self.wait.until(
            lambda driver: driver.current_url
            and "checkout-step-two.html" in driver.current_url
        )

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_item_name(self):
        return self.get_text(self.ITEM_NAME)

    def get_item_price(self):
        return self.get_text(self.ITEM_PRICE)

    def get_item_total(self):
        return self.get_text(self.ITEM_TOTAL)

    def get_tax(self):
        return self.get_text(self.TAX)

    def get_total(self):
        return self.get_text(self.TOTAL)

    def finish_checkout(self):
        finish_button = self.wait.until(
            lambda driver: driver.find_element(
                *self.FINISH_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            finish_button
        )

        self.wait.until(
            lambda driver: driver.current_url
            and "checkout-complete.html" in driver.current_url
        )

    def cancel_checkout(self):
        self.click(self.CANCEL_BUTTON)

    def get_confirmation_message(self):
        return self.get_text(self.COMPLETE_HEADER)

    def get_confirmation_text(self):
        return self.get_text(self.COMPLETE_TEXT)

    def back_home(self):
        self.click(self.BACK_HOME_BUTTON)
