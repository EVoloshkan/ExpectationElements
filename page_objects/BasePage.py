import logging
import os
import allure

from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.__config_logger()

    def __config_logger(self, to_file=True):
        self.logger = logging.getLogger(type(self).__name__)
        os.makedirs("logs", exist_ok=True)
        if to_file:
            file_handler = logging.FileHandler(f"logs/{self.driver.test_name}.log")
            file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.driver.log_level)

    @allure.step
    def click(self, element):
        self.logger.info(f"Clicking element: {element}")
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    @allure.step
    def _input(self, element, value):
        self.click(element)
        self.logger.info(f"Clear element: {element}")
        element.clear()
        self.logger.info(f"Input send_keys: {value}")
        element.send_keys(value)

    @allure.step
    def alert(self):
        self.logger.info(f"Switch to alert accept")
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    @allure.step
    def element(self, locator: tuple):
        try:
            self.logger.info(f"Search element: {locator}")
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"Timeout Exception: {locator}")

            with allure.step("Attach screenshot"):
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="Screenshot",
                    attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    @allure.step
    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        self.logger.info(f"Search element in element: {parent_locator}, {child_locator}")
        return self.element(parent_locator).find_element(*child_locator)

    @allure.step
    def elements(self, locator: tuple):
        try:
            self.logger.info(f"Search elements: {locator}")
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error(f"Timeout Exception: {locator}")
            raise AssertionError(f"Не дождался видимости элементов {locator}")


