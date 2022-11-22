import os
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--url", default="https://demo-opencart.ru", help="This is request url")
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--driver_path", action="store", default="")
    parser.addoption("--log_level", default="ERROR")
    parser.addoption("--executor", action="store", default="192.168.1.70")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--videos", action="store_true")
    parser.addoption("--bv")


@pytest.fixture
def browser(request):
    url = request.config.getoption("--url")
    browser = request.config.getoption("--browser")
    driver_path = request.config.getoption("--driver_path")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    mobile = request.config.getoption("--mobile")

    if executor == "local":
        caps = {'goog:chromeOptions': {}}

        if mobile:
            caps["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}

        if browser == "safari":
            driver = webdriver.Safari(desired_capabilities=caps)
        elif browser == "chrome":
            if driver_path == "":
                driver_path = os.path.expanduser("~/Downloads/drivers/chromedriver")
            driver = webdriver.Chrome(executable_path=driver_path, desired_capabilities=caps)
        else:
            raise ValueError(f"Incorrect driver {browser}")

    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser,
            "browserVersion": version,
            # "screenResolution": "1280x720",
            "name": "Mikhail",
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
            'goog:chromeOptions': {}
        }

        if browser == "chrome" and mobile:
            caps["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

    if not mobile:
        driver.maximize_window()

    driver.base_url = url
    driver.log_level = log_level
    driver.test_name = request.node.name

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
