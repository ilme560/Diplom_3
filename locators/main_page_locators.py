from selenium.webdriver.common.by import By


class MainPageLocators:
    # кнопка "Конструктор" в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")

    # кнопка "Лента заказов" в шапке
    ORDERS_FEED_BUTTON = (By.LINK_TEXT, 'Лента Заказов')

    # кнопка Личный кабинет в шапке
    PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, 'Личный Кабинет')

    # Заголовок главной страницы "Собери бургер"
    TITLE_IN_THE_MAIN_PAGE = (By.XPATH, '//h1[contains(@class, "text text_type_main-large")]')

    # Заголовок в ленте заказов
    ORDERS_FEED_HEAD = (By.XPATH, '//h1[contains(text(),"Лента заказов")]')

    # ингридиент
    INGREDIENT = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")

    # Заголовок окна с деталями об ингредиенте
    INGREDIENT_DETAILS_HEAD = (By.XPATH, '//h2[text()="Детали ингредиента"]')

    # кнопка крестик в окне с деталями об ингредиенте
    CLOSE_BUTTON = (By.XPATH, "(//button[@type='button'])[1]")

    # корзина конструктора
    BASKET = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_")

    # счетчик ингредиента
    INGREDIENT_COUNTER = (By.XPATH, '//p[contains(@class, "counter")]')

    # кнопка Оформить заказ
    ORDER_BUTTON = (By.XPATH, '//button[contains(@class,"button_button__33qZ0" )]')

    # заголовок окна после оформления заказа
    ORDER_WINDOW = (By.XPATH, "//div[@class='Modal_modal__container__Wo2l_']")

    # карточка заказа в Ленте заказов
    ORDER_CARD = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")

    # окно с деталями о заказе
    ORDER_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")

    # номер заказа в ленте и в истории
    ORDER_NUMBER = (By.XPATH, '//p[contains(@class, "text text_type_digits")]')

    # cчетчик заказов за все время
    ALL_TIME_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[1]")

    # счетчик закзов за день
    DAY_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")

    # номер заказа в окне после создания
    ORDER_ID = (By.XPATH, "//p[contains(text(),'идентификатор заказа')]")

    # раздел "В работе"
    SECTION_IN_WORK = (By.XPATH, f"//li[contains(text(), '0')]")
