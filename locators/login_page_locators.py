from selenium.webdriver.common.by import By


class LoginPageLocators:

    # заголовок страници входа в "Личный кабинет"
    LOGIN_HEAD = (By.XPATH, "//h2[text()='Вход']")

    # поле ввода email на странице авторизации
    EMAIL_INPUT_FIELD_LOGIN = (By.XPATH, "//input[@name = 'name']")

    # поле ввода пароля на странице авторизации
    PASSWORD_INPUT_FIELD_LOGIN = (By.XPATH, "//input[@name = 'Пароль']")

    # кнопка Войти на странице авторизации
    LOGIN_BUTTON = (By.XPATH, './/button[text() = "Войти"]')

    # кнопка восстановления пароля
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")

    # Заголовок странице авторизации
    TITLE_ENTER = By.TAG_NAME, 'h2'
