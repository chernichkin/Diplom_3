import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderPageLocators


class OrderFeedPage(BasePage):

    @allure.step('Ожидаем видимость списка заказов')
    def check_first_order_in_list_is_visible(self):
        self.check_element_is_visable(OrderPageLocators.first_order_in_list)

    @allure.step('Кликаем по первому элементу списка заказов')
    def click_on_first_order_in_list(self):
        self.click_on_element(OrderPageLocators.first_order_in_list)

    @allure.step('Ждем всплывающее окно с деталями заказа')
    def order_details_window_is_clickable(self):
        self.check_element_is_visable(OrderPageLocators.popup_order_window)

    @allure.step('Проверяем что открылось окно "Детали заказа"')
    def check_show_details_window(self):
        if self.driver.find_element(*OrderPageLocators.popup_order_window):
            return True
        else:
            return False

    @allure.step('Считываем значение счетчика "Выполнено за всё время"')
    def get_count_all_time(self):
        return int(self.driver.find_element(*OrderPageLocators.all_time_counter_value).text)

    @allure.step('Считываем значение счетчика "Выполнено за сегодня"')
    def get_count_today(self):
        return int(self.driver.find_element(*OrderPageLocators.today_counter_value).text)

    @allure.step('Получение заказа по номеру в разделе "В работе"')
    def get_order_number_in_work(self):
        self.get_text_element(OrderPageLocators.order_in_work)