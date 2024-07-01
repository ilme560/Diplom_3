import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажатие на кнопку "Личный кабинет"')
    def click_on_personal_account(self):
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Нажатие на кнопку "Конструктор"')
    def click_on_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Проверка что отображается раздел "Конструктор"')
    def check_constructor_section(self):
        assert self.get_value(MainPageLocators.TITLE_IN_THE_MAIN_PAGE) == 'Соберите бургер'

    @allure.step('Нажатие на кнопку "Лента заказов"')
    def click_on_orders_feed(self):
        self.click_on_element(MainPageLocators.ORDERS_FEED_BUTTON)

    @allure.step('Проверка что отображается раздел "Лента заказов"')
    def check_orders_feed_section(self):
        return self.get_value(MainPageLocators.ORDERS_FEED_HEAD)

    @allure.step('Нажатие на ингредиент')
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT)

    @allure.step('Проверка что отображается всплывающее окно с деталями об ингредиенте')
    def check_ingredient_details_window(self):
        assert self.find_element_with_wait(MainPageLocators.INGREDIENT_DETAILS_HEAD).text == 'Детали ингредиента'

    @allure.step('Закрытие всплывающего окно с деталями об ингредиенте')
    def close_details_window(self):
        self.click_on_element(MainPageLocators.CLOSE_BUTTON)

    @allure.step('Проверка что всплывающее окно с деталями об ингредиенте закрыто')
    def check_close_ingredient_details_window(self):
        assert self.element_is_not_displayed(MainPageLocators.INGREDIENT_DETAILS_HEAD)

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredients_to_order(self):
        self.drag_and_drop_on_element(MainPageLocators.INGREDIENT, MainPageLocators.BASKET)

    @allure.step('Получение значения из счетчика ингредиента')
    def get_ingredient_counter(self):
        return self.get_value(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Нажатие на кнопку "Оформить заказ"')
    def click_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Проверка что  открылось окно об успешно оформленном заказе')
    def check_order_window(self):
        assert self.find_element_with_wait(MainPageLocators.ORDER_WINDOW).is_displayed()

    @allure.step('Нажатие на карточку заказа в Ленте заказов')
    def click_on_order_card(self):
        self.click_on_element(MainPageLocators.ORDER_CARD)

    @allure.step('Проверка что  открылось окно с деталями о заказе')
    def check_order_details_window(self):
        assert self.find_element_with_wait(MainPageLocators.ORDER_DETAILS).is_displayed()

    @allure.step('Получение значения счетчика "Выполнено за всё время"')
    def get_count_all_time(self):
        return self.find_element_with_wait(MainPageLocators.ALL_TIME_COUNTER).text

    @allure.step('Получение значения счетчика "Выполнено за сегодня"')
    def get_count_day(self):
        return self.find_element_with_wait(MainPageLocators.DAY_COUNTER).text

    @allure.step('Получение номера заказа в всплывающем окне после оформления заказа')
    def get_order_id(self):
        return self.find_element_with_wait(MainPageLocators.ORDER_ID)

    @allure.step('Получение текущего номера заказа в разделе "В работе"')
    def get_order_from_section_in_work(self):
        return self.element_is_present(MainPageLocators.SECTION_IN_WORK).text
