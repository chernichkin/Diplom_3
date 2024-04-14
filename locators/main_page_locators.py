from selenium.webdriver.common.by import By


class MainPageLocators:

    login_main_button = [By.XPATH, './/button[text()= "Войти в аккаунт"]']
    profile_button = [By.XPATH, './/a[@href= "/account"]']

