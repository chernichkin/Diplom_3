import pytest
import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.recovery_page import RecoveryPage
from pages.reset_password_page import ResetPasswordPage
from constants import Constants, Data


class TestMainFunctions:

    @pytest.mark.parametrize(
        'driver', ['driver_chrome', 'driver_firefox']
    )
    @allure.title('Проверка перехода на страницу конструктора')
    def test_redirect_constructor_after_click_true(self, request, driver):
        driver = request.getfixturevalue(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        main_page.check_button_profile_is_clickable()
        main_page.click_on_profile_button()
        profile_page.check_button_login_is_visible()
        main_page.click_on_constructor_button()
        main_page.check_login_main_btn_is_visible()
        text_title = main_page.get_text_title()
        assert text_title == 'Соберите бургер'

    @pytest.mark.parametrize(
        'driver', ['driver_chrome', 'driver_firefox']
    )
    @allure.title('Проверка перехода на страницу ленты заказов')
    def test_redirect_order_feed_after_click_true(self, request, driver):
        driver = request.getfixturevalue(driver)
        main_page = MainPage(driver)
        main_page.check_login_main_btn_is_visible()
        main_page.click_on_order_feed_button()
        main_page.check_done_title_is_visible()
        text_title = main_page.get_text_title()
        assert text_title == 'Лента заказов'

    @pytest.mark.parametrize(
        'driver', ['driver_chrome', 'driver_firefox']
    )
    @allure.title('Проверка появления попапа после клика по ингредиенту')
    def test_click_on_ingredient_open_popup(self, request, driver):
        driver = request.getfixturevalue(driver)
        main_page = MainPage(driver)
        main_page.check_first_ingredient_is_visible()
        main_page.click_on_first_ingredient()
        main_page.check_popup_title_is_visible()
        text_title_popup = main_page.get_text_title_popup()
        assert text_title_popup == 'Детали ингредиента'

    @pytest.mark.parametrize(
        'driver', ['driver_chrome', 'driver_firefox']
    )
    @allure.title('Проверка закрытия попапа с ингредиентом крестиком')
    def test_click_on_x_closed_popup(self, request, driver):
        driver = request.getfixturevalue(driver)
        main_page = MainPage(driver)
        main_page.check_first_ingredient_is_visible()
        main_page.click_on_first_ingredient()
        main_page.check_popup_title_is_visible()
        main_page.click_on_close_popup_btn()
        main_page.check_login_main_btn_is_clickable()
        text_title = main_page.get_text_title()
        assert text_title == 'Соберите бургер'
