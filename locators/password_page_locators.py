from selenium.webdriver.common.by import By


class PasswordPageLocators:
    # поле ввода для email на странице восстановления пароля
    RECOVERY_EMAIL = (By.XPATH, './/input[@name = "name"]')

    # кнопка восстановить на странице восстановления пароля
    RECOVERY_BUTTON = (By.XPATH, './/button[ text() = "Восстановить"]')

    # заголовок "Восстановление пароля"
    PASSWORD_RECOVERY_HEAD = (By.XPATH, "//h2[text()='Восстановление пароля']")

    # кнопка "Показать пароль"
    PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")

    # поле Пароль активно
    PASSWORD_FIELD_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")
