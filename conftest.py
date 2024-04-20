import pytest
import requests
from selenium import webdriver
from constants import Endpoints
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from helper import generate_payloads


@pytest.fixture()
def driver_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()


@pytest.fixture()
def driver_firefox():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def create_user_and_delete():
    payload = generate_payloads()
    response = requests.post(Endpoints.URL + Endpoints.REGISTER, data=payload)
    token = response.json()['accessToken']
    yield payload['email'], payload['password']
    headers = {'Authorization': token}
    requests.delete(Endpoints.URL + Endpoints.USER, headers=headers)


@pytest.fixture(scope='function')
def create_user_login_and_delete(request, driver, create_user_and_delete):
    driver = request.getfixturevalue(driver)
    email, password = create_user_and_delete
    main_page = MainPage(driver)
    profile_page = ProfilePage(driver)
    main_page.check_button_profile_is_clickable()
    main_page.click_on_profile_button()
    profile_page.check_button_login_is_visible()
    profile_page.set_email(email)
    profile_page.set_password(password)
    profile_page.click_on_login_btn()
    main_page.check_button_profile_is_clickable()
    main_page.click_on_profile_button()
    profile_page.check_btn_save_is_visible()
    yield main_page, profile_page




