from selenium.webdriver.common.by import By


class BasePageLocators:
    logo = [By.XPATH, '//div[@class= "AppHeader_header__logo__2D0X2"]/a']
    main_title = [By.XPATH, "//h1"]
    constructor_btn = [By.XPATH, "//p[text()='Конструктор']"]
    order_feed_btn = [By.XPATH, "//p[text()='Лента Заказов']"]
