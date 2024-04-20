import pytest
import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestProfile:

    @pytest.mark.parametrize(
        'driver', ['driver_chrome', 'driver_firefox']
    )
    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_profile_login_is_visible_true(self, request, driver):
        driver = request.getfixturevalue(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        main_page.check_button_profile_is_clickable()
        main_page.click_on_profile_button()
        profile_page.check_recovery_button_profile_is_clickable()
        profile_page.check_button_login_is_visible()
        text_login_btn = profile_page.get_text_login_button()
        assert text_login_btn == 'Войти'

    @pytest.mark.parametrize(
        'driver', ['driver_chrome', 'driver_firefox']
    )
    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_move_to_order_history(self, request, driver, create_user_and_delete):
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
        profile_page.click_on_history_btn_profile()
        attr_history_btn = profile_page.get_attribute_history_btn()
        assert attr_history_btn == "page"

    @pytest.mark.parametrize(
        'driver', ['driver_chrome', 'driver_firefox']
    )
    @allure.title('Проверка выхода из аккаунта')
    def test_exit_from_profile_true(self, driver, create_user_login_and_delete):
        main_page, profile_page = create_user_login_and_delete
        profile_page.check_exit_btn_is_clickable()
        profile_page.click_on_exit_btn_profile()
        profile_page.check_button_login_is_visible()
        text_login_btn = profile_page.get_text_login_button()
        assert text_login_btn == "Войти"
