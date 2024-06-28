import allure
from locators.password_page_locators import PasswordPageLocators
from pages.base_page import BasePage


class RestorePasswordPage(BasePage):

    @allure.step('Заполнение поля "Email"')
    def fill_email(self):
        email = 'ilme560@yandex.ru'
        self.add_text_to_element(PasswordPageLocators.RECOVERY_EMAIL, email)

    @allure.step('Нажатие на кнопку "Восстановить"')
    def click_on_restore_button(self):
        self.click_on_element(PasswordPageLocators.RECOVERY_BUTTON)

    @allure.step('Проверка что кнопка "Показать/скрыть пароль" отображается')
    def check_show_password_button(self):
        assert self.find_element_with_wait(PasswordPageLocators.PASSWORD_BUTTON).is_displayed()

    @allure.step('Нажатие на кнопку "Показать/скрыть пароль"')
    def click_show_password_button(self):
        self.click_on_element(PasswordPageLocators.PASSWORD_BUTTON)

    @allure.step('Проверка что поле "Пароль" активно')
    def check_active_field_password(self):
        assert self.find_element_with_wait(PasswordPageLocators.PASSWORD_FIELD_ACTIVE).is_displayed()
