import pytest
import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage
from helper import list_compare


class TestOrderFeed:

    @pytest.mark.parametrize(
        'driver', ['driver_chrome', 'driver_firefox']
    )
    @allure.title('Проверка перехода на страницу конструктора')
    def test_popup_open_after_click_true(self, request, driver):
        driver = request.getfixturevalue(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.check_order_feed_btn_is_clickable()
        main_page.click_on_order_feed_button()
        order_feed_page.check_first_order_in_list_is_visible()
        order_feed_page.click_on_first_order_in_list()
        order_feed_page.order_details_window_is_clickable()
        assert order_feed_page.check_show_details_window() == True

    @pytest.mark.parametrize(
        'driver', ['driver_chrome', 'driver_firefox']
    )
    @allure.title('Проверка отображания заказов из раздела «История заказов» на странице «Лента заказов»')
    def test_check_history_orders_into_orders_food_success(self, request, driver, create_user_and_delete):
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
        main_page.check_order_btn_is_visible()
        main_page.add_bun_to_order_basket()
        main_page.click_on_order_btn()
        main_page.check_x_btn_order_popup_is_clickable()
        main_page.check_order_status_text_is_visible()
        main_page.check_order_default_status_text_is_visible()
        main_page.click_on_x_btn_order_popup()
        main_page.click_on_profile_button()
        profile_page.check_btn_save_is_visible()
        profile_page.click_on_history_btn_profile()
        profile_page.check_orders_history_profile_is_visible()
        profile_list = profile_page.get_list_orders_user()
        main_page.click_on_order_feed_button()
        main_page.check_done_title_is_visible()
        all_list = main_page.get_list_orders()
        assert list_compare(profile_list, all_list)


    @pytest.mark.parametrize(
        'driver', ['driver_chrome', 'driver_firefox']
    )
    @allure.title('Проверка увеличения счётчика "Выполнено за всё время" при создании заказа')
    def test_check_increasing_counter_all_time_value_success(self, request, driver, create_user_and_delete):
        driver = request.getfixturevalue(driver)
        email, password = create_user_and_delete
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        order_page = OrderFeedPage(driver)
        main_page.check_button_profile_is_clickable()
        main_page.click_on_profile_button()
        profile_page.check_button_login_is_visible()
        profile_page.set_email(email)
        profile_page.set_password(password)
        profile_page.click_on_login_btn()
        main_page.check_order_btn_is_visible()
        main_page.click_on_order_feed_button()
        main_page.check_done_title_is_visible()
        current_count = order_page.get_count_all_time()
        main_page.click_on_constructor_button()
        main_page.check_order_btn_is_visible()
        main_page.add_bun_to_order_basket()
        main_page.click_on_order_btn()
        main_page.check_x_btn_order_popup_is_clickable()
        main_page.check_order_status_text_is_visible()
        main_page.check_order_default_status_text_is_visible()
        main_page.click_on_x_btn_order_popup()
        main_page.check_order_btn_is_visible()
        main_page.click_on_order_feed_button()
        main_page.check_done_title_is_visible()
        new_count = order_page.get_count_all_time()

        assert (new_count - current_count) == 1

    @pytest.mark.parametrize(
        'driver', ['driver_chrome', 'driver_firefox']
    )
    @allure.title('Проверка что после оформления заказа его номер появляется в разделе "В работе"')
    def test_check_increasing_counter_today_value_success(self, request, driver, create_user_and_delete):
        driver = request.getfixturevalue(driver)
        email, password = create_user_and_delete
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        order_page = OrderFeedPage(driver)
        main_page.check_button_profile_is_clickable()
        main_page.click_on_profile_button()
        profile_page.check_button_login_is_visible()
        profile_page.set_email(email)
        profile_page.set_password(password)
        profile_page.click_on_login_btn()
        main_page.check_order_btn_is_visible()
        main_page.add_bun_to_order_basket()
        main_page.click_on_order_btn()
        main_page.check_x_btn_order_popup_is_clickable()
        main_page.check_order_status_text_is_visible()
        main_page.check_order_default_status_text_is_visible()
        order = main_page.get_order_number()
        main_page.click_on_x_btn_order_popup()
        main_page.click_on_order_feed_button()
        main_page.check_done_title_is_visible()
        order_in_work = order_page.get_order_number_in_work()

        assert order in order_in_work


