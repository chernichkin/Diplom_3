import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.recovery_page_locators import RecoveryPageLocators
from locators.reset_password_locators import ResetPasswordLocators


class ResetPasswordPage(BasePage):

    @allure.step('Проверяем видимость кнопки "Сохранить"')
    def check_btn_save_is_visible(self):
        self.check_element_is_visable(ResetPasswordLocators.btn_save)

    @allure.step('Получаем текст кнопки "Сохранить"')
    def get_text_btn_save(self):
        return self.get_text_element(ResetPasswordLocators.btn_save)

    @allure.step('Кликаем по кнопке "показать/скрыть пароль"')
    def click_on_eye_btn(self):
        self.click_on_element(ResetPasswordLocators.btn_eye)

    @allure.step('Получить значение атрибута поля ввода email')
    def get_attribute_email_input(self):
        return self.get_attribute_element(ResetPasswordLocators.email, 'type')

