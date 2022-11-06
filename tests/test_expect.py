from page_objects.AdminPage import AdminPage
from page_objects.HomePage import HomePage
from page_objects.RegisterPage import RegisterPage


def test_admin_add_product(driver, base_url):
    AdminPage(driver, base_url) \
        .redirect().login("demo", "demo") \
        .redirect_to_add_product() \
        .create_product("Phone", "IPhone")


def test_admin_delete_product(driver, base_url):
    AdminPage(driver, base_url) \
        .redirect() \
        .login("demo", "demo"). \
        delete_product()


def test_registration_user(driver, base_url):
    RegisterPage(driver, base_url) \
        .move_to_registration_form() \
        .registration_user(
            "TestUser123456",
            "TestUser654321",
            "testmail35745645@mail.ru",
            "+79990000000",
            "testuser111")


def test_switch_currency(driver, base_url):
    HomePage(driver, base_url).switch_currency("RUB")
