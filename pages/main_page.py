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


class MainPage(BasePage):

    @allure.step('Проверяем что кнопка личного кабинета доступна для клика')
    def check_button_login_is_clickable(self):
        self.check_element_is_clickable(MainPageLocators.profile_button)

    @allure.step('Кликаем по кнопке "Личный кабинет"')
    def click_on_profile_button(self):
        self.click_on_element(MainPageLocators.profile_button)



