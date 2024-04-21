from selenium.webdriver.common.by import By


class ProfilePageLocators:

    login_button_profile = [By.XPATH, '//button[text()= "Войти"]'] #Кнопка Войти
    recovery_button_profile = [By.XPATH, './/a[text()= "Восстановить пароль"]'] #Кнопка восстановить пароль
    save_btn = [By.XPATH, '//button[text()= "Сохранить"]'] #Кнопка сохранить
    email_input = [By.XPATH, '//input[@name= "name"]'] #Поле ввода email
    password_input = [By.XPATH, '//input[@name= "Пароль"]'] #Поле ввода пароля
    history_btn = [By.XPATH, './/a[@href= "/account/order-history"]'] #Кнопка истории
    exit_btn = [By.XPATH, '//button[text()="Выход"]'] #Кнопка Выйти
    history_list_profile = [By.XPATH, ".//div[contains(@class,'OrderHistory_textBox')]/p[contains(@class,'text_type_digits')]"]

