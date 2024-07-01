from faker import Faker

import allure


@allure.step('Создаем данные для регистрации')
def get_sign_up_date():
    fake = Faker()
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name()
    }
    return user_data

