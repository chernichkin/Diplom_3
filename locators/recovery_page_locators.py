from selenium.webdriver.common.by import By


class RecoveryPageLocators:

    recovery_button = [By.XPATH, '//button[text()= "Восстановить"]'] #Кнопка восстановить пароль
    email = [By.XPATH, '//input[@name="name"]'] #Поле email