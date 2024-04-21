import allure
from pages.base_page import BasePage
from locators.recovery_page_locators import RecoveryPageLocators


class RecoveryPage(BasePage):

    @allure.step('Проверяем видимость кнопки восстановления')
    def check_recovery_button_is_visible(self):
        self.check_element_is_visable(RecoveryPageLocators.recovery_button)

    @allure.step('Получаем текст кнопки восстановления')
    def get_text_recovery_button(self):
        return self.get_text_element(RecoveryPageLocators.recovery_button)

    @allure.step('Вводим почту')
    def set_name(self, email):
        self.set_field_by_locator(RecoveryPageLocators.email, email)

    @allure.step('Кликаем по кнопке восстановления')
    def click_on_recovery_button(self):
        self.click_on_element(RecoveryPageLocators.recovery_button)

    @allure.step('Вводим данные почты')
    def set_email(self, email):
        self.set_field_by_locator(RecoveryPageLocators.email, email)

