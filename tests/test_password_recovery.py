import pytest
import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.recovery_page import RecoveryPage
from pages.reset_password_page import ResetPasswordPage
from constants import Constants, Data


class TestPasswordRecovery:

    @pytest.mark.parametrize(
        'driver', ['driver_chrome', 'driver_firefox']
    )
    def test_profile_login_is_visible_true(self, request, driver):
        driver = request.getfixturevalue(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.check_button_login_is_clickable()
        main_page.click_on_profile_button()
        profile_page.check_recovery_button_profile_is_clickable()
        profile_page.click_on_recovery_button_profile()
        recovery_page.check_recovery_button_is_visible()
        text_login_btn = recovery_page.get_text_recovery_button()
        assert text_login_btn == Constants.RECOVERY_TEXT

    @pytest.mark.parametrize(
        'driver,email',
        [
            ['driver_chrome', 'amassma@gmail.com'],
            ['driver_chrome', 'sasasa@yandex.ru'],
            ['driver_firefox', 'amassma@gmail.com'],
            ['driver_firefox', 'sasasa@yandex.ru']
        ]
    )
    def test_redirect_after_recovery_true(self, request, driver, email):
        driver = request.getfixturevalue(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        recovery_page = RecoveryPage(driver)
        reset_pass_page = ResetPasswordPage(driver)
        main_page.check_button_login_is_clickable()
        main_page.click_on_profile_button()
        profile_page.check_recovery_button_profile_is_clickable()
        profile_page.click_on_recovery_button_profile()
        recovery_page.check_recovery_button_is_visible()
        recovery_page.set_email(email)
        recovery_page.click_on_recovery_button()
        reset_pass_page.check_btn_save_is_visible()
        text_btn_save = reset_pass_page.get_text_btn_save()
        assert text_btn_save == 'Сохранить'

    @pytest.mark.parametrize(
        'driver', ['driver_chrome', 'driver_firefox']
    )
    def test_field_is_active_after_click_true(self, request, driver, email='amassma@gmail.com'):
        driver = request.getfixturevalue(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        recovery_page = RecoveryPage(driver)
        reset_pass_page = ResetPasswordPage(driver)
        main_page.check_button_login_is_clickable()
        main_page.click_on_profile_button()
        profile_page.check_recovery_button_profile_is_clickable()
        profile_page.click_on_recovery_button_profile()
        recovery_page.check_recovery_button_is_visible()
        recovery_page.set_email(email)
        recovery_page.click_on_recovery_button()
        reset_pass_page.check_btn_save_is_visible()
        reset_pass_page.click_on_eye_btn()
        type_email_field = reset_pass_page.get_attribute_email_input()
        assert type_email_field == 'text'


