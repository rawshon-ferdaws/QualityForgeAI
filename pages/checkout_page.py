from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def enter_first_name(self, first_name):
        self.type(
            self.FIRST_NAME_INPUT,
            first_name
        )

    def enter_last_name(self, last_name):
        self.type(
            self.LAST_NAME_INPUT,
            last_name
        )

    def enter_postal_code(self, postal_code):
        self.type(
            self.POSTAL_CODE_INPUT,
            postal_code
        )

    def enter_customer_information(
        self,
        first_name,
        last_name,
        postal_code
    ):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue(self):
        self.click(
            self.CONTINUE_BUTTON
        )

    def click_finish(self):
        self.click(
            self.FINISH_BUTTON
        )

    def get_success_message(self):
        return self.get_text(
            self.SUCCESS_MESSAGE
        )

    def get_error_message(self):
        return self.get_text(
            self.ERROR_MESSAGE
        )
