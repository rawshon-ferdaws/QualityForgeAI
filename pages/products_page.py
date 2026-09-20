from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):

    PAGE_TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_page_title(self):
        return self.get_text(
            self.PAGE_TITLE
        )

    def add_backpack_to_cart(self):
        self.click(
            self.ADD_BACKPACK_BUTTON
        )

    def remove_backpack_from_cart(self):
        self.click(
            self.REMOVE_BACKPACK_BUTTON
        )

    def get_cart_count(self):
        return self.get_text(
            self.CART_BADGE
        )

    def open_cart(self):
        self.click(
            self.CART_ICON
        )
