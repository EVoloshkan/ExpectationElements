import os.path

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://demo-opencart.ru",
        help="This is request url"
    )
    parser.addoption(
        "--driver",
        default="Safari",
        help="This is default browser"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def driver(request):
    str_driver = request.config.getoption("--driver")
    if str_driver == "Safari":
        driver = webdriver.Safari()
    elif str_driver == "Chrome":
        driver = webdriver.Chrome(executable_path=os.path.expanduser("~/Downloads/drivers/chromedriver"))
    elif str_driver == "FireFox":
        driver = webdriver.Chrome(executable_path=os.path.expanduser("~/Downloads/drivers/geckodriver"))
    elif str_driver == "Opera":
        driver = webdriver.Chrome(executable_path=os.path.expanduser("~/Downloads/drivers/operadriver"))
    else:
        raise ValueError(f"Incorrect driver {str_driver}")

    driver.maximize_window()

    yield driver

    driver.close()
