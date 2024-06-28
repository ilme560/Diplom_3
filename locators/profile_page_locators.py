from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # кнопка "Профиль"
    PROFILE_BUTTON = (By.LINK_TEXT, 'Профиль')

    # кнопка "История заказов
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, 'История заказов')

    # кнопка Выход в Личном кабинете
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # кнопка Сохранить в Личном кабинете
    SAVE_BUTTON = By.XPATH, "//button[contains(text(),'Сохранить')]"
