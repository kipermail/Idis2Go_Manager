import selectors
import pytest
from faker import Faker
#from I2G.models.user import User
from models.user import User
#from pages.user import User_page
from helpers.columns_helper import BaseColumns
from helpers.filters_helper import BaseFilters


@pytest.fixture
def new_user():
    fake = Faker()
    return User(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        password=fake.password(),
        language=fake.random_element(elements=('RU', 'EN', 'DE', 'UA')), 
        role=fake.random_element(elements=('Distributor administrator', 'Customer administrator', 'Customer user')),
        distributor=fake.random_element(elements=('DEMO', 'PROD')),
        customer=fake.random_element(elements=('Clinic', 'Clinic QA2')),
        is_active=fake.boolean(),
        is_doctor=fake.boolean(),
        email_verified=fake.boolean()
    )
    


def user_with_custom_fields(new_user, **kwargs):
    for key, value in kwargs.items():
        setattr(new_user, key, value)
    return new_user

# def test_empty_email(new_user):
#     user = user_with_custom_fields(new_user, email="")
#     assert user.email == ""

class UserColumns(BaseColumns):

    # CHECK_COLUMN_EMAIL = ('input[value="email"]')
    # CHECK_COLUMN_EMAIL_VERIFIED = ('#setup_dialog_base_user_table input[value="email_verified"]')
    # CHECK_COLUMN_FIRST_NAME = ('#setup_dialog_base_user_table input[value="first_name"]')
    # CHECK_COLUMN_LAST_NAME = ('#setup_dialog_base_user_table input[value="last_name"]')
    # CHECK_COLUMN_ROLE = ('#setup_dialog_base_user_table input[value="role"]')
    # CHECK_COLUMN_DISTRIBUTOR = ('#setup_dialog_base_user_table input[value="distributor"]')
    # CHECK_COLUMN_IS_ACTIVE = ('#setup_dialog_base_user_table input[value="is_active"]')
    # CHECK_COLUMN_IS_STAFF = ('#setup_dialog_base_user_table input[value="is_staff"]')
    # CHECK_COLUMN_IS_SUPERUSER = ('#setup_dialog_base_user_table input[value="is_superuser"]')
    # CHECK_COLUMN_IS_DOCTOR = ('#setup_dialog_base_user_table input[value="is_doctor"]')
    # CHECK_COLUMN_ACTIONS = ('#setup_dialog_base_user_table input[value="actions"]')
    SAVE_BUTTON = ('input[name="_save_column_setup"]')
    CLOSE_ICON  = ('#ModalColumn button.close')

    def __init__(self, page):
        """ 
        The class represents user's columns with the state of activity (active) 
        and availability (enabled).
        """
        columns = [
            ("email", False, False),
            ("email_verified", False, True),
            ("first_name", False, False),
            ("last_name", False, False),
            ("role", False, True),
            ("distributor", False, True),
            ("is_active", False, True),
            ("is_staff", False, True),
            ("is_superuser", False, True),
            ("is_doctor", False, True),
            ("actions", False, False)
        ]
        super().__init__(columns, page)




class UserFilters(BaseFilters):
    def __init__(self, page):
        fields = [
            ("is_archive", True),
            ("is_active", True),
            ("email_verified", True),
            ("roles", True),
            ("distributor", True),
            ("customer", True),
        ]
        super().__init__(fields, page)



    # 
# Пример использования:
# driver = webdriver.Chrome()
# user_columns = get_user_columns(driver)

# Активируем только email и role, остальные должны быть деактивированы
# active_fields = ['email', 'role']
# set_user_columns(driver, user_columns, active_fields)

# # Пример использования:
# user_columns = UserColumns()

# # Установим активность для email
# user_columns.set_active('email', True)

# # Отключим доступность для поля role
# user_columns.set_enabled('role', False)

# print(user_columns)


#    def set_active(self, column, active):
#         if hasattr(self, column):
#             getattr(self, column)["active"] = active
#         else:
#             raise ValueError(f"Column '{column}' does not exist.")

#     def is_active_(self, column):
#         if hasattr(self, column):
#             return getattr(self, column)["active"]
#         else:
#             raise ValueError(f"Column '{column}' does not exist.")      

#     def is_enabled(self, column):
#         if hasattr(self, column):
#             return getattr(self, column)["enabled"]
#         else:
#             raise ValueError(f"Column '{column}' does not exist.")

    #def get_checkbox_selector(self, field_name):
    #     """Возвращает селектор для чекбокса по его имени."""
    #     return f'label:has(input[value="{field_name}"])'
    
    # def set_user_columns(self, page, active_fields):
    #     """
    #     Устанавливает состояние чекбоксов на веб-форме в зависимости от списка активных полей.
    #     :param page: Экземпляр страницы для взаимодействия с браузером.
    #     :param active_fields: Список полей, которые должны быть активными (остальные деактивируются).
    #     """
    #     current_columns = UserColumns()
    #     current_columns.get_user_columns(page)
        
    #     for field_name in current_columns.__dict__:
    #         selector = self.get_checkbox_selector(field_name)
    #         if field_name in active_fields:
    #             self.enable_checkbox(page, selector)  
    #         else:
    #             self.disable_checkbox(page, selector)  

    # def get_checkbox_state(self, page: User_page, field_name):
    #     """Получает текущее состояние (active и enabled) для чекбокса."""
    #     selector = self.get_checkbox_selector(field_name)
    #     checkbox = page.page.locator(selector)
        
    #     is_checked = checkbox.is_checked()
    #     is_enabled = checkbox.is_enabled()
        
    #     return {'active': is_checked, 'enabled': is_enabled}

    # def get_user_columns(self, page: User_page):
    #     """Собирает состояние всех чекбоксов в экземпляре UserColumns."""
    #     user_columns = UserColumns()
        
    #     for field_name in user_columns.__dict__:
    #         checkbox_state = self.get_checkbox_state(page, field_name)
    #         setattr(user_columns, field_name, checkbox_state)
        
    #     return user_columns

    # def enable_checkbox(self, page: User_page, field_name):
    #     """Включает чекбокс, если он неактивен и доступен для изменения."""
    #     checkbox_state = self.get_checkbox_state(page, field_name)
        
    #     if checkbox_state["enabled"] and not checkbox_state["active"]:
    #         selector = self.get_checkbox_selector(field_name)
    #         page.page.locator(selector).check()

    # def disable_checkbox(self, page: User_page, field_name):
    #     """Выключает чекбокс, если он активен и доступен для изменения."""
    #     checkbox_state = self.get_checkbox_state(page, field_name)
        
    #     if checkbox_state["enabled"] and checkbox_state["active"]:
    #         selector = self.get_checkbox_selector(field_name)
    #         page.page.locator(selector).uncheck()
