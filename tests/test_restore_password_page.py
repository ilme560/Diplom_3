import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.password_page import RestorePasswordPage


class TestRestorePassword:
    @allure.title('Проверка раздела «Восстановление пароля»')
    @allure.description('Проверка на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_restore_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        login_page = LoginPage(driver)
        login_page.click_on_restore_password_button()
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.check_password_recovery_head()

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
        restore_password_page.check_show_password_button()

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
