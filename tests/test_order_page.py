import allure
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeed:


    @allure.title('Проверка раздела «Лента заказов»')
    @allure.description('Проверка что при нажатии на заказ, открывается всплывающее окно с деталями о заказе')
    def test_open_order_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_orders_feed()
        main_page.click_on_order_card()
        main_page.check_order_details_window()

    @allure.title('Проверка раздела «Лента заказов»')
    @allure.description('Проверка что заказы пользователя из раздела «История заказов» отображаются на странице «Лента '
                  'заказов»')
    def test_order_number_from_history_orders_in_orders_feed(self, driver, login):
        main_page = MainPage(driver)
        main_page.add_ingredients_to_order()
        main_page.click_order_button()
        main_page.close_details_window()
        main_page.click_on_personal_account()
        profile_page = PersonalAccountPage(driver)
        profile_page.click_on_order_history_button()
        profile_page.check_order_in_order_feed()

    @allure.title('Проверка раздела «Лента заказов»')
    @allure.description('Проверка что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_all_time_increased_after_new_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_on_orders_feed()
        current_value = main_page.get_count_all_time()
        main_page.click_on_constructor()
        main_page.add_ingredients_to_order()
        main_page.click_order_button()
        main_page.close_details_window()
        main_page.click_on_orders_feed()
        updated_value = main_page.get_count_all_time()
        assert updated_value > current_value

    @allure.title('Проверка раздела «Лента заказов»')
    @allure.description('Проверка что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_counter_day_increased_after_new_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_on_orders_feed()
        current_value = main_page.get_count_day()
        main_page.click_on_constructor()
        main_page.add_ingredients_to_order()
        main_page.click_order_button()
        main_page.close_details_window()
        main_page.click_on_orders_feed()
        updated_value = main_page.get_count_day()
        assert updated_value > current_value

    @allure.title('Проверка раздела «Лента заказов»')
    @allure.description('Проверка что после оформления заказа его номер появляется в разделе В работе')
    def test_order_number_in_section_in_work(self, driver, login):
        main_page = MainPage(driver)
        main_page.add_ingredients_to_order()
        main_page.click_order_button()
        order_number = main_page.get_order_id()
        main_page.close_details_window()
        main_page.click_on_orders_feed()
        order_number_in_work = main_page.get_order_from_section_in_work()
        assert int(order_number_in_work) == int(order_number)
