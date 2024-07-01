import allure
from locators.profile_page_locators import ProfilePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import Urls


class PersonalAccountPage(BasePage):

    @allure.step('Нажимаем на кнопку "История заказов"')
    def click_on_order_history_button(self):
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Проверка открытия раздела "История заказов"')
    def check_order_history_section(self):
        current_url = self.get_current_url()
        assert current_url == Urls.ORDER_HISTORY

    @allure.step('Нажимаем на кнопку "Выход"')
    def click_on_logout_button(self):
        self.click_on_element(ProfilePageLocators.EXIT_BUTTON)

    @allure.step('Проверка истории заказов')
    def check_order_in_order_feed(self):
        order_history = self.get_value(MainPageLocators.ORDER_NUMBER)
        order_feed = self.get_value(MainPageLocators.ORDER_NUMBER)
        assert order_history == order_feed

    @allure.step('Проверка что открылась страница "Личный кабинет"')
    def check_profile_button(self):
        assert self.find_element_with_wait(ProfilePageLocators.PROFILE_BUTTON).is_displayed()
