import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def check_element_is_clickable(self, locator):
        WebDriverWait(self.driver, 8).until(
            expected_conditions.element_to_be_clickable(locator))

    def wait_invisibility_element(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.invisibility_of_element_located(locator))

    def check_element_is_visable(self, locator):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Скроллим вниз страницы')
    def scroll_to_down_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_to_target_by_id(self, locator_id):
        self.driver.find_element(By.ID, locator_id).click()

    def get_text_in_target_by_id(self, locator_id):
        return self.driver.find_element(By.ID, locator_id).text

    def get_text_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Смена страниц')
    def switch_pages(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains('https://dzen.ru/'))

    @allure.step('Получение текущего url')
    def get_current_url(self):
        return self.driver.current_url

    def set_field_by_locator(self, locator, key):
        self.driver.find_element(*locator).send_keys(key)

    @allure.step('Получение атрибута')
    def get_class_element(self, locator):
        self.driver.find_element(*locator).get_attribute('class')

    def get_attribute_element(self, locator, attribute):
        return self.driver.find_element(*locator).get_attribute(attribute)

    @allure.step('Перетаскивание элемента')
    def drag_and_drop_element(self, locator_from, locator_to):
        self.check_element_is_visable(locator_from)
        self.check_element_is_visable(locator_to)
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script("""
                   var source = arguments[0];
                   var target = arguments[1];
                   var evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
               """, element_from, element_to)
