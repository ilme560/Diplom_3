import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.password_page import RestorePasswordPage
from locators.password_page_locators import PasswordPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRestorePassword:
    @allure.title('Проверка раздела «Восстановление пароля»')
    @allure.description('Проверка на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_restore_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        login_page = LoginPage(driver)
        login_page.click_on_restore_password_button()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(PasswordPageLocators.PASSWORD_RECOVERY_HEAD))
        assert driver.find_element(*PasswordPageLocators.PASSWORD_RECOVERY_HEAD).text == 'Восстановление пароля'

    @allure.title('Проверка раздела «Восстановление пароля»')
    @allure.description('Проверка ввода почты и клика по кнопке «Восстановить»')
    def test_email_input_and_clicking_on_restore_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        login_page = LoginPage(driver)
        login_page.click_on_restore_password_button()
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.fill_email()
        restore_password_page.click_on_restore_button()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(PasswordPageLocators.PASSWORD_BUTTON))
        password_button = driver.find_element(*PasswordPageLocators.PASSWORD_BUTTON)
        assert password_button.is_displayed()

    @allure.title('Проверка раздела «Восстановление пароля»')
    @allure.description('Проверка клика по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_click_on_password_button_makes_field_active(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        login_page = LoginPage(driver)
        login_page.click_on_restore_password_button()
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.fill_email()
        restore_password_page.click_on_restore_button()
        restore_password_page.click_show_password_button()
        restore_password_page.check_active_field_password()
