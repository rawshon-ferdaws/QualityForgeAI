from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.config_reader import ConfigReader


class BasePage:

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            ConfigReader.get_explicit_wait()
        )

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        def get_element_text(driver):
            try:
                text = driver.find_element(*locator).text
                return text if text else False
            except StaleElementReferenceException:
                return False

        return self.wait.until(get_element_text)

    def is_visible(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return bool(element and element.is_displayed())

    def is_present(self, locator):
        return len(
            self.driver.find_elements(*locator)
        ) > 0
