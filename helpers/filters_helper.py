from playwright.sync_api import Page
#from pages.user import User_page
import re




class BaseFilters:

    APPLAY_BUTTON = ('input[name="form_filter"]')
    CLEAR_BUTTON = ('input[id="clear-form"]')
    CLOSE_ICON  = ('#ModalColumn button.close')
    DROPDOWN_SINGLE = ('.select2-selection--single')
    DROPDOWN_MULTYPLE = ('.select2-selection--multiple')
    
    DROPDOWN_RESULT = ('.select2-results__option')

    ROLES = {
    'Superuser': 'superuser',
    'Regional manager': 'regional_manager',
    'Customer administrator': 'customer_administrator',
    'Service engineer': 'service_engineer',
    'Customer user': 'customer_user',
    'Distributor administrator': 'distributor_administrator',
    }

    def __init__(self, fields, page: Page):
        """
        Инициализация атрибутов на основе переданных полей.
        :param fields: Список кортежей (имя поля, доступный).
        """
        self.page = page
        for field_name, enabled in fields:
            setattr(self, field_name, {"enabled": enabled, "values": []})
    

    def close_filters_form(self):
        self.page.locator(self.CLOSE_ICON).click()
        self.page.wait_for_load_state()

    def applay_filters_form(self):
        self.page.locator(self.APPLAY_BUTTON).click()
        self.page.wait_for_load_state()

    def reset_filters_form(self):
        self.page.locator(self.CLEAR_BUTTON).click()
        self.page.wait_for_load_state()


    def open_dropdown(self, field_id):
        selector = f'{self.DROPDOWN_SINGLE}[aria-labelledby*="{field_id}"]'
        self.page.locator(selector).click()

    def select_single_option(self, option_text):
        self.page.wait_for_selector(self.DROPDOWN_RESULT)
        selector = f'{self.DROPDOWN_RESULT}[id*="{option_text}"]'
        self.page.locator(selector).click() 
   
    
    def select_multiple_options(self, options_list):
        for option_text in options_list:  
            self.select_single_option(option_text)

    def set_filter_state(self, field: str, option):
        """
        Устанавливает состояние фильтра на веб-форме в зависимости от поля и списка значений.
        :param page: Экземпляр страницы для взаимодействия с браузером.
        :param field: Поле, которое должно быть установлено.
        :param option: Значение для поля field.
        """
        form_filters = self 
        for field_name in form_filters.__dict__:
            if field_name == "page":  continue
            if field_name in field:
                self.open_dropdown(field_name)
                self.select_single_option(option)       

    def set_filter_multiple_state(self, field: str, options):
        """
        Устанавливает состояние фильтра на веб-форме в зависимости от поля и списка значений.
        :param field: Список полей, которые должны быть установлены.
        :param options: Список полей для списка field.
        """
        form_filters = self 
        for field_name in form_filters.__dict__:
            if field_name == "page":  continue
            if field_name in field:
                for option_text in options:  
                    if option_text in self.ROLES:
                        option_text = self.ROLES[option_text]
                    else:
                        print(f"Role {option_text} is not valid")
                    #self.open_dropdown(page, field_name)
                    self.page.locator(self.DROPDOWN_MULTYPLE).click()
                    self.select_single_option(option_text)  

    def set_filter_date_state(self, field: str, option: str):
        """
        Устанавливает состояние фильтра на веб-форме в зависимости от поля и списка значений.
        :param field:  поле, которое должно быть установлено.
        :param option:  поле для field.
        """
        form_filters = self 
        for field_name in (field,) : #form_filters.__dict__:
            if field_name == "page":  continue
            if field_name in (field,):
                    #self.open_dropdown(page, field_name)
                    self.page.pause()
                    select = self.page.locator(f'input[id="id_{field_name}"]')
                    print("sel", select, option)
                    select.click()
                    select.fill("2024-10-20")
                    # select.clear()
                    # select.fill(option)
                    select.press("Enter")  
                    


    def __repr__(self):
            return '\n'.join([f"{col}: {getattr(self, col)}" for col in self.__dict__])



    #def enable_checkbox(self, page, field_name):
    #     """Включает чекбокс, если он неактивен и доступен для изменения."""
    #     checkbox_state = self.get_checkbox_state(page, field_name)
        
    #     if checkbox_state["enabled"] and not checkbox_state["active"]:
    #         selector = self.get_checkbox_selector(field_name)  
    #         self.page.locator(selector).check()

    # def disable_checkbox(self, page, field_name):
    #     """Выключает чекбокс, если он активен и доступен для изменения."""
    #     checkbox_state = self.get_checkbox_state(page, field_name)
        
    #     if checkbox_state["enabled"] and checkbox_state["active"]:
    #         selector = self.get_checkbox_selector(field_name)  
    #         self.page.locator(selector).uncheck()

    # def get_checkbox_selector(self, field_name):
    #     """Возвращает селектор для чекбокса на основе имени поля."""
    #     return f'label:has(input[value="{field_name}"])'

    # def get_checkbox_state(self, page, field_name):
    #     """Получает текущее состояние чекбокса."""
    #     selector = self.get_checkbox_selector(field_name)
    #     checkbox = self.page.locator(selector)
        
    #     is_checked = checkbox.is_checked()
    #     is_enabled = checkbox.is_enabled()
        
    #     return {'active': is_checked, 'enabled': is_enabled}        

    # def get_columns_state(self, page):
    #     """Собирает состояние всех чекбоксов в экземпляре FormColumns."""
    #     form_columns = self 
    #     for field_name in form_columns.__dict__:
    #         checkbox_state = self.get_checkbox_state(page, field_name)
    #         setattr(form_columns, field_name, checkbox_state)
        
    #     return form_columns

    # def set_columns_state(self, page, active_fields):
    #     """
    #     Устанавливает состояние чекбоксов на веб-форме в зависимости от списка активных полей.
    #     :param page: Экземпляр страницы для взаимодействия с браузером.
    #     :param active_fields: Список полей, которые должны быть активными (остальные деактивируются).
    #     """
    #     form_columns = self 
    #     form_columns.get_columns_state(page)
        
    #     for field_name in form_columns.__dict__:
    #         #selector = self.get_checkbox_selector(field_name)
    #         if field_name in active_fields:
    #             self.enable_checkbox(page, field_name)  
    #         else:
    #             self.disable_checkbox(page, field_name)  
