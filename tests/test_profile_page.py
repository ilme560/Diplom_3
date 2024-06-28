import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPersonalAccount:
    @allure.title('Проверка раздела «Личный кабинет »')
    @allure.description('Проверка перехода по клику на «Личный кабинет»')
    def test_go_to_personal_account(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_BUTTON))
        profile_button = driver.find_element(*ProfilePageLocators.PROFILE_BUTTON)
        assert profile_button.is_displayed()

    @allure.title('Проверка раздела «Личный кабинет »')
    @allure.description('Проверка перехода в раздел «История заказов»')
    def test_go_to_order_history_in_personal_account(self, driver, login, ):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        profile_page = PersonalAccountPage(driver)
        profile_page.click_on_order_history_button()
        profile_page.check_order_history_section()

    @allure.title('Проверка раздела «Личный кабинет »')
    @allure.description('Проверка выхода из аккаунта')
    def test_logout(self, driver, login):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_on_personal_account()
        profile_page = PersonalAccountPage(driver)
        profile_page.click_on_logout_button()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        assert driver.find_element(*LoginPageLocators.TITLE_ENTER).text == 'Вход'
