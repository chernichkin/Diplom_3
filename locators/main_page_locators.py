from selenium.webdriver.common.by import By


class MainPageLocators:

    login_main_button = [By.XPATH, './/button[text()= "Войти в аккаунт"]']
    profile_button = [By.XPATH, './/a[@href= "/account"]']
    order_main_btn = [By.XPATH, './/button[text()= "Оформить заказ"]']
    done_title = [By.XPATH, "//p[text()='Готовы:']"]
    bun_01 = [By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"]
    h2_popup = [By.XPATH, '//h2[contains(@class, "Modal_modal__title_modified__3Hjkd")]']
    x_popup_btn = [By.XPATH, '//h2[contains(@class, "Modal_modal__title_modified__3Hjkd")]']
    x_popup_btn_offer = [By.XPATH, '//button[contains(@class, "Modal_modal__close_modified__3V5XS")]']
    sauce_02 = [By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]']
    bun_1 = [By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d]']
    burger_drop_place = [By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']"]
    counter_sauce = [By.XPATH, "//img[@alt='Соус Spicy-X']/parent::*//p[@class='counter_counter__num__3nue1']"]
    start_order_title = [By.XPATH, './/p[text()= "идентификатор заказа"]']
    order_list_all = [By.XPATH, ".//div[contains(@class,'OrderHistory_textBox')]/p[contains(@class,'text_type_digits')]"]
    order_status_text = [By.XPATH, '//p[text()="Ваш заказ начали готовить"]']
    default_order_number = [By.XPATH, '//h2[text()="9999"]']
    current_order_number = [By.XPATH, '//*[contains(@class, "type_digits-large")]']
