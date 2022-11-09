import allure
from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class HomePage(BasePage):
    CURRENCY_MENU = (By.CSS_SELECTOR, "#form-currency > div > button")
    EUR_CURRENCY = (By.NAME, "EUR")
    GBP_CURRENCY = (By.NAME, "GBP")
    USD_CURRENCY = (By.NAME, "USD")
    RUB_CURRENCY = (By.NAME, "RUB")

    def switch_currency(self, currency):
        self.driver.get(self.base_url)
        self.click(self.element(self.CURRENCY_MENU))

        with allure.step(f"Валюта {currency}"):
            pass

        if currency == "EUR":
            self.click(self.element(self.EUR_CURRENCY))
        elif currency == "GBP":
            self.click(self.element(self.GBP_CURRENCY))
        elif currency == "USD":
            self.click(self.element(self.USD_CURRENCY))
        elif currency == "RUB":
            self.click(self.element(self.RUB_CURRENCY))
        else:
            self.logger.error(f"Currency not found: {currency}")
            raise ValueError(f"Неизвестная валюта {currency}")
        return self
