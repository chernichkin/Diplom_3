from selenium.webdriver.common.by import By


class ResetPasswordLocators:

    email = [By.XPATH, '//input[@name="Введите новый пароль"]']  # Поле ввода пароля
    btn_save = [By.XPATH, './/button[text()= "Сохранить"]']
    btn_eye = [By.CLASS_NAME, 'input__icon']

