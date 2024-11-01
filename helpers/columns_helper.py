from playwright.sync_api import Page


class BaseColumns():

    SAVE_BUTTON = ('input[name="_save_column_setup"]')
    CLOSE_ICON  = ('#ModalColumn button.close')

    def __init__(self, columns, page: Page):
        """
        Инициализация атрибутов на основе переданных полей.
        :param fields: Список кортежей (имя поля, активный, доступный).
        """
        self.page = page
        for column_name, active, enabled in columns:
            setattr(self, column_name, {"active": active, "enabled": enabled})

    def enable_checkbox(self, field_name):
        """Включает чекбокс, если он неактивен и доступен для изменения."""
        checkbox_state = self.get_checkbox_state(field_name)
        
        if checkbox_state["enabled"] and not checkbox_state["active"]:
            selector = self.get_checkbox_selector(field_name)  
            self.page.locator(selector).check()

    def disable_checkbox(self, field_name):
        """Выключает чекбокс, если он активен и доступен для изменения."""
        checkbox_state = self.get_checkbox_state(field_name)
        
        if checkbox_state["enabled"] and checkbox_state["active"]:
            selector = self.get_checkbox_selector(field_name)  
            self.page.locator(selector).uncheck()

    def get_checkbox_selector(self, field_name):
        """Возвращает селектор для чекбокса на основе имени поля."""
        return f'label:has(input[value="{field_name}"])'

    def get_checkbox_state(self, field_name):
        """Получает текущее состояние чекбокса."""
        selector = self.get_checkbox_selector(field_name)
        checkbox = self.page.locator(selector)
        
        is_checked = checkbox.is_checked()
        is_enabled = checkbox.is_enabled()
        
        return {'active': is_checked, 'enabled': is_enabled}        

    def get_columns_state(self):
        """Собирает состояние всех чекбоксов в экземпляре FormColumns."""
        form_columns = self 
        for field_name in form_columns.__dict__:
            if field_name == "page":  continue
            checkbox_state = self.get_checkbox_state(field_name)
            setattr(form_columns, field_name, checkbox_state)
        
        return form_columns

    def set_columns_state(self, active_fields):
        """
        Устанавливает состояние чекбоксов на веб-форме в зависимости от списка активных полей.
        :param page: Экземпляр страницы для взаимодействия с браузером.
        :param active_fields: Список полей, которые должны быть активными (остальные деактивируются).
        """
        form_columns = self 
        #form_columns.get_columns_state()
        
        for field_name in form_columns.__dict__:
            if field_name == "page":  continue
            #selector = self.get_checkbox_selector(field_name)
            if field_name in active_fields:
                self.enable_checkbox(field_name)  
            else:
                self.disable_checkbox(field_name)  


    def close_columns_form(self):
        self.page.locator(self.CLOSE_ICON).click()

    def save_columns_form(self):
        self.page.locator(self.SAVE_BUTTON).click()





    def __repr__(self):
            return '\n'.join([f"{col}: {getattr(self, col)}" for col in self.__dict__])
