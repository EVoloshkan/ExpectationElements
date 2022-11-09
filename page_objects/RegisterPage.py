from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class RegisterPage(BasePage):
    LK_USER_MENU = (By.CSS_SELECTOR, "#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md")
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, "#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a")
    FIRSTNAME_INPUT = (By.ID, "input-firstname")
    LASTNAME_INPUT = (By.ID, "input-lastname")
    EMAIL_INPUT = (By.ID, "input-email")
    PHONE_NUMBER_INPUT = (By.ID, "input-telephone")
    PASSWORD_INPUT = (By.ID, "input-password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "input-confirm")
    CHECK_BOX_AGREE = (By.CSS_SELECTOR, '#content > form > div > div > input[type="checkbox"]:nth-child(3)')
    REGISTRATION_USER_BUTTON = (By.CSS_SELECTOR, "#content > form > div > div > input.btn.btn-primary")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#content > div > div > a")

    def move_to_registration_form(self):
        self.driver.get(self.base_url)
        self.click(self.element(self.LK_USER_MENU))
        self.click(self.element(self.REGISTER_FORM_BUTTON))
        return self

    def registration_user(self, firstname, lastname, email, phone, password):
        self._input(self.element(self.FIRSTNAME_INPUT), firstname)
        self._input(self.element(self.LASTNAME_INPUT), lastname)
        self._input(self.element(self.EMAIL_INPUT), email)
        self._input(self.element(self.PHONE_NUMBER_INPUT), phone)
        self._input(self.element(self.PASSWORD_INPUT), password)
        self._input(self.element(self.CONFIRM_PASSWORD_INPUT), password)
        self.driver.execute_script("window.scrollTo(0, 1080)")
        self.click(self.element(self.CHECK_BOX_AGREE))
        self.click(self.element(self.REGISTRATION_USER_BUTTON))
        self.click(self.element(self.CONTINUE_BUTTON))
        return self


