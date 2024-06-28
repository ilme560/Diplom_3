import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.main_page import MainPage
from pages.login_page import LoginPage
from helpers import get_sign_up_date
from data import Urls


def _get_driver(name):
    if name == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        return webdriver.Chrome(service=service)
    elif name == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        return webdriver.Firefox(service=service)
    else:
        raise TypeError("Driver is not found")


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = _get_driver(request.param)
    driver.set_window_size(1920, 1080)
    driver.get(Urls.URL_BASE)
    yield driver
    driver.quit()


@pytest.fixture
def user_registration():
    payload = get_sign_up_date()
    response = requests.post(Urls.CREATING_A_USER, json=payload)
    token = response.json().get('accessToken')
    yield payload, token

    headers = {'Authorization': f'Bearer {token}'}
    requests.delete(Urls.CHANGING_USER_DATA, headers=headers)


@pytest.fixture
def login(driver, user_registration):
    payload, token = user_registration
    email = payload["email"]
    password = payload["password"]
    main_page = MainPage(driver)
    main_page.click_on_personal_account()
    login_page = LoginPage(driver)
    login_page.login(email, password)
    return driver
