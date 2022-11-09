import allure
import pytest

from page_objects.Admin1Page import Admin1Page
from page_objects.HomePage import HomePage
from page_objects.RegisterPage import RegisterPage


@allure.feature("Admin Page")
@allure.title("Add a new product in admin page")
@allure.link("https://github.com/EVoloshkan/ExpectationElements", name="My Github")
def test_admin_add_product(driver, base_url):
    Admin1Page(driver, base_url) \
        .redirect().login("demo", "demo") \
        .redirect_to_add_product() \
        .create_product("Phone", "IPhone")


@allure.title("Delete a product in admin page")
def test_admin_delete_product(driver, base_url):
    Admin1Page(driver, base_url) \
        .redirect() \
        .login("demo", "demo"). \
        delete_product()


@allure.step
@allure.feature("New customer registration")
def test_registration_user(driver, base_url):
    RegisterPage(driver, base_url) \
        .move_to_registration_form() \
        .registration_user(
            "TestUser123456",
            "TestUser654321",
            "testmail35745645@mail.ru",
            "+79990000000",
            "testuser111")


# @pytest.mark.skip(reason="Bug-000")
@pytest.mark.parametrize("currency", ["USD", "RUB", "CHF"])
def test_switch_currency(driver, base_url, currency):
    HomePage(driver, base_url).switch_currency(currency)
