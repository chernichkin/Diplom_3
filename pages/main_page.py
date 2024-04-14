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
    def check_button_profile_is_clickable(self):
        self.check_element_is_clickable(MainPageLocators.profile_button)

    @allure.step('Кликаем по кнопке "Личный кабинет"')
    def click_on_profile_button(self):
        self.click_on_element(MainPageLocators.profile_button)

    @allure.step('Кликаем по кнопке "Конструктор"')
    def click_on_constructor_button(self):
        self.click_on_element(BasePageLocators.constructor_btn)

    @allure.step('Получаем текст заголовка')
    def get_text_title(self):
        return self.get_text_element(BasePageLocators.main_title)

    @allure.step('Ожидаем видимость кнопки "Оформить заказ"')
    def check_order_btn_is_visible(self):
        self.check_element_is_visable(MainPageLocators.order_main_btn)

    @allure.step('Ожидаем видимость кнопки "Войти в аккаунт"')
    def check_login_main_btn_is_visible(self):
        self.check_element_is_visable(MainPageLocators.login_main_button)

    @allure.step('Ожидаем кликабельность кнопки "Войти в аккаунт"')
    def check_login_main_btn_is_clickable(self):
        self.check_element_is_clickable(MainPageLocators.login_main_button)

    @allure.step('Кликаем по кнопке "Лента заказов"')
    def click_on_order_feed_button(self):
        self.click_on_element(BasePageLocators.order_feed_btn)

    @allure.step('Ожидаем видимость кнопки "Войти в аккаунт"')
    def check_done_title_is_visible(self):
        self.check_element_is_visable(MainPageLocators.done_title)

    @allure.step('Ожидаем видимость первого ингредиента')
    def check_first_ingredient_is_visible(self):
        self.check_element_is_visable(MainPageLocators.bun_01)

    @allure.step('Кликаем по первому ингредиенту')
    def click_on_first_ingredient(self):
        self.click_on_element(MainPageLocators.bun_01)

    @allure.step('Ожидаем видимость заголовка в попапе')
    def check_popup_title_is_visible(self):
        self.check_element_is_visable(MainPageLocators.h2_popup)

    @allure.step('Получаем текст заголовка в попапе')
    def get_text_title_popup(self):
        return self.get_text_element(MainPageLocators.h2_popup)

    @allure.step('Кликаем по крестику в попапе')
    def click_on_close_popup_btn(self):
        self.click_on_element(MainPageLocators.x_popup_btn)

