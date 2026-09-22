from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):

    # Locators
    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")

    ADD_BACKPACK_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test='add-to-cart-sauce-labs-backpack']"
    )

    REMOVE_BACKPACK_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test='remove-sauce-labs-backpack']"
    )

    BACKPACK_NAME = (
        By.CSS_SELECTOR,
        "[data-test='inventory-item-name']"
    )

    # Actions
    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def is_products_page_displayed(self):
        return self.get_page_title() == "Products"

    def get_product_count(self):
        return len(
            self.driver.find_elements(*self.INVENTORY_ITEMS)
        )

    def add_backpack_to_cart(self):
        add_button = self.wait.until(
            lambda driver: driver.find_element(
                *self.ADD_BACKPACK_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_button
        )

        def cart_badge_updated(driver):
            element = driver.find_element(
                *self.CART_BADGE
            )

            if element is None:
                return False

            return element.text == "1"

        self.wait.until(cart_badge_updated)

    def remove_backpack_from_cart(self):
        remove_button = self.wait.until(
            lambda driver: driver.find_element(
                *self.REMOVE_BACKPACK_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            remove_button
        )

        self.wait.until(
            lambda driver: len(
                driver.find_elements(*self.CART_BADGE)
            ) == 0
        )

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)

    def is_cart_badge_present(self):
        return self.is_present(
            self.CART_BADGE
        )

    def open_cart(self):
        cart_link = self.wait.until(
            lambda driver: driver.find_element(
                *self.CART_LINK
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            cart_link
        )

        self.wait.until(
            lambda driver: driver.current_url
            and "cart.html" in driver.current_url
        )
