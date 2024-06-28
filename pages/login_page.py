import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage (BasePage):

    @allure.step('Нажатие на кнопку "Восстановить пароль"')
    def click_on_restore_password_button(self):
        self.click_on_element(LoginPageLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step('Авторизация на сайте')
    def login(self, email, password):
        self.add_text_to_element(LoginPageLocators.EMAIL_INPUT_FIELD_LOGIN, email)
        self.add_text_to_element(LoginPageLocators.PASSWORD_INPUT_FIELD_LOGIN, password)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)
