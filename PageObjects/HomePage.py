import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Utilities.BasePage import BasePage


class HomePage(BasePage):
    """By locators"""
    CURRENCY_DROPDOWN = (By.XPATH, "//select[@id='customerCurrency']")

    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)

    """Action Methodes"""

    def page_title(self, title):
        return self.get_title(title)

    def get_default_currency(self):
        select = Select(self.driver.find_element(*self.CURRENCY_DROPDOWN))
        default_currency = select.first_selected_option.text
        return default_currency

