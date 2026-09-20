from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")

    def get_item_name(self):
        return self.get_text(
            self.CART_ITEM_NAME
        )

    def click_checkout(self):
        self.click(
            self.CHECKOUT_BUTTON
        )

    def continue_shopping(self):
        self.click(
            self.CONTINUE_SHOPPING_BUTTON
        )

    def remove_backpack(self):
        self.click(
            self.REMOVE_BACKPACK_BUTTON
        )
