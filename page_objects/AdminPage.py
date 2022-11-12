import allure

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    PATH = "/admin"
    LOGIN_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "div.text-right > button")
    CATALOG_MENU = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCTS_MENU = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2) > a")
    ADD_PRODUCT = (By.CSS_SELECTOR, "#content > div.page-header > div > div > a")
    CATEGORY_INPUT = (By.ID, "input-name1")
    TEG_INPUT = (By.ID, "input-meta-title1")
    SAVE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "#content > div.page-header > div > div > button")
    CHECK_BOX_CHOICE = (
        By.CSS_SELECTOR,
        '#form-product > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > input[type="checkbox"]')
    DELETE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "#content > div.page-header > div > div > button.btn.btn-danger")

    @property
    def path(self):
        return self.base_url + self.PATH

    @allure.step("Redirect to admin authorization page")
    def redirect(self):
        self.driver.get(self.path)
        return self

    @allure.step("Input login and password")
    def login(self, login, password):
        self._input(self.element(self.LOGIN_INPUT), login)
        self._input(self.element(self.PASSWORD_INPUT), password)
        self.click(self.element(self.LOGIN_BUTTON))
        return self

    @allure.step("Redirect to add new product form")
    def redirect_to_add_product(self):
        self.click(self.element(self.CATALOG_MENU))
        self.click(self.element(self.PRODUCTS_MENU))
        self.click(self.element(self.ADD_PRODUCT))
        return self

    @allure.step("Tap a button to create product")
    def create_product(self, category, teg):
        self._input(self.element(self.CATEGORY_INPUT), category)
        self._input(self.element(self.TEG_INPUT), teg)
        self.click(self.element(self.SAVE_PRODUCT_BUTTON))
        return self

    @allure.step("Tap a button to delete product")
    def delete_product(self):
        self.click(self.element(self.CATALOG_MENU))
        self.click(self.element(self.PRODUCTS_MENU))
        self.click(self.element(self.CHECK_BOX_CHOICE))
        self.click(self.element(self.DELETE_PRODUCT_BUTTON))
        self.alert()
        return self
