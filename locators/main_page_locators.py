from selenium.webdriver.common.by import By


class MainPageLocators:

    login_main_button = [By.XPATH, './/button[text()= "Войти в аккаунт"]']
    profile_button = [By.XPATH, './/a[@href= "/account"]']
    order_main_btn = [By.XPATH, './/button[text()= "Оформить заказ"]']
    done_title = [By.XPATH, "//p[text()='Готовы:']"]
    bun_01 = [By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"]
    h2_popup = [By.XPATH, '//h2[contains(@class, "Modal_modal__title_modified__3Hjkd")]']
    x_popup_btn = [By.XPATH, '//h2[contains(@class, "Modal_modal__title_modified__3Hjkd")]']
