from playwright.sync_api import Page
####from I2G.pages.base_page import Base_page
from pages.base_page import Base_page

class Login_page(Base_page):
    
    PAGE_URL =  "/login/"

    def __init__(self, page: Page):
        super().__init__(page)  # Вызов __init__ родительского класса
        #self.page = page
        self.csrf_token = ''
        # self.login = "john_snow@mailinator.com"
        # self.password = "Idisov147"
    


    def login_user(self, login, password):
        self.page.wait_for_selector('form.login-form')
        email_field = self.page.locator('.login-form >> input[id="id_username"]')
        password_field = self.page.locator('.login-form >> input[id="id_password"]')
        submit_button = self.page.locator('.login-form >> button[type="submit"]')
        csrf_token = self.page.query_selector('.login-form >> input[name="csrfmiddlewaretoken"]')
        
        self.csrf_token = csrf_token.get_attribute('value')
        email_field.fill(login)
        password_field.fill(password)
        submit_button.click()
        self.page.wait_for_load_state('networkidle')   


    def restore_password(self, user: str):
        self.user = user
        pass 

    def has_error_messages(self):
        """Check for the required error messages to the email and password fields.
        Returns `True` if any of the error messages are visible"""
        email_error = self.page.query_selector('.login-form__email >> p.error-pill')
        password_error = self.page.query_selector('.login-form__password >> p.error-pill')
        email_required = email_error.is_visible() if email_error else False
        password_required = password_error.is_visible() if password_error else False
        return email_required or password_required

    def has_alert_message(self):
        """Checks for a invalid Email or Password message. 
        Returns `True` if the alert message is visible"""
        login_error = self.page.query_selector('.login-form >> div.alert-warning')
        invalid_login = login_error.is_visible() if login_error else False 
        return invalid_login