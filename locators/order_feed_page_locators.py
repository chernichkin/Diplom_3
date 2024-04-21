from selenium.webdriver.common.by import By


class OrderPageLocators:
    first_order_in_list = [By.XPATH, './/li[contains(@class,"OrderHistory_listItem__2x95r")][1]']
    order_is_done_title = [By.XPATH, './/p[text()= "Выполнен"]']
    x_feed_popup_btn = [By.XPATH, '//button[contains(@class, "Modal_modal__close_modified__3V5XS")]']
    popup_order_window = [By.XPATH, ".//div[contains(@class,'Modal_orderBox')]/p"]
    all_time_counter_value = [By.XPATH, ".//p[text()='Выполнено за все время:']/../p[contains(@class,'OrderFeed_number')]"]
    today_counter_value = [By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"digits-large")]']
    order_in_work = [By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]'] #Заказы в работе
