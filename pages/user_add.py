import re
from playwright.sync_api import Page
from pages.base_page import Base_page

class Add_user_page(Base_page):
    
    PAGE_URL =  "/user/add/"

    
    LNAME_FIELD = ('.panel-body >> input[id="id_last_name"]')
    FNAME_FIELD = ('.panel-body >> input[id="id_first_name"]')
    EMAIL_FIELD = ('.panel-body >> input[id="id_email"]')
    PASSWORD_FIELD = ('.panel-body >> input[id="id_password"]')
    ISACTIVE_FIELD = ('label[for="id_is_active"]')
    EMAIL_VERIFIED_FIELD = ('label[for="id_email_verified"]')
    ISDOCTOR_FIELD = ('label[for="id_is_doctor"]')
    LANGUAGE_FIELD = ('span.select2-selection[aria-labelledby*=email_language]')
    LANGUAGE_LIST = ('li.select2-results__option')
    CUSTOMER_FIELD = ('span.select2-selection[aria-labelledby*=customer]')
    DISTRIBUTOR_FIELD = ('span.select2-selection[aria-labelledby*=distributor]')
    CUSTOMER_LIST = ('li.select2-results__option')
    DISTRIBUTOR_LIST = ('li.select2-results__option')
    ROLE_FIELD = ('span.select2-selection[aria-labelledby*=id_role]')
    ROLE_LIST = ('li.select2-results__option')
    SAVE_BUTTON = ('.panel-footer button[data-js-id="save-button"]')
    CANCEL_BUTTON = ('.panel-footer input[data-js-id="cancel-button"]')
    CLOSE_ICON = ('.panel-header a[href="/user/"]')
    ROLES = {
    'Superuser': 'superuser',
    'Regional manager': 'regional_manager',
    'Customer administrator': 'customer_administrator',
    'Service engineer': 'service_engineer',
    'Customer user': 'customer_user',
    'Distributor administrator': 'distributor_administrator',
}

    
    def __init__(self, page: Page):
        self.page = page

    def enter_first_name(self, first_name: str):
        self.page.locator(self.FNAME_FIELD).fill(first_name)
        
    def enter_last_name(self, last_name: str):
        self.page.locator(self.LNAME_FIELD).fill(last_name)

    def enter_email(self, email: str):
        self.page.locator(self.EMAIL_FIELD).fill(email)

    def enter_password(self, password: str):
        self.page.locator(self.PASSWORD_FIELD).fill(password)

    def select_is_active(self, is_active: bool):
        if is_active:
            self.page.wait_for_selector(self.ISACTIVE_FIELD).click()
        #self.page.wait_for_selector('label[for="id_is_active"]').click()

    def select_email_verified(self, is_verified: bool):
        if is_verified:
            self.page.wait_for_selector(self.EMAIL_VERIFIED_FIELD).click()   

    def select_language(self, language: str):
        self.page.locator(self.LANGUAGE_FIELD).click()
        #self.page.wait_for_timeout(1000)
        self.page.wait_for_selector('.select2-results')
        self.page.locator(self.LANGUAGE_LIST, has_text=language).click()
         
    def select_role(self, role: str):
        self.page.locator(self.ROLE_FIELD).click()
        self.page.wait_for_selector('.select2-results')
        #self.page.wait_for_timeout(1000)
        #self.page.locator(self.ROLE_LIST, has_text='Customer user').click()
        if role in self.ROLES:
            role_list = f'{self.ROLE_LIST}[id*={self.ROLES[role]}]'
            self.page.locator(role_list).click()
        else:
            print("Role is not valid")
    
             

    def select_is_doctor(self, is_doctor: bool):
        if is_doctor: 
            self.page.wait_for_selector(self.ISDOCTOR_FIELD).click() 
    
    def is_doctor_visible(self):
        return self.page.locator(self.ISDOCTOR_FIELD,).is_visible(timeout=100)
    
    def is_customer_visible(self):
        return self.page.locator(self.CUSTOMER_FIELD,).is_visible(timeout=100)
    
    def is_distributor_visible(self):
        return self.page.locator(self.DISTRIBUTOR_FIELD,).is_visible(timeout=100)

    def select_customer(self, customer: str):
        self.page.locator(self.CUSTOMER_FIELD).click()
        #self.page.locator('span.select2-selection[aria-labelledby*=customer]').click()
        self.page.wait_for_load_state()
        options = self.page.locator(self.CUSTOMER_LIST)
        for option in options.all():
            text = option.inner_text()
            if re.match(rf'^{customer}$', text):
                option.click()
                break
        else:
            print("Customer not found in list")    
        #self.page.locator(self.CUSTOMER_LIST, has_text="Clinic QA2").click()        

    def select_distributor(self, distributor: str):
        self.page.locator(self.DISTRIBUTOR_FIELD).click()
        self.page.wait_for_load_state()
        options = self.page.locator(self.DISTRIBUTOR_LIST)
        for option in options.all():
            text = option.inner_text()
            if re.match(rf'^{distributor}$', text):
                option.click()
                break
        else:
            print("Distriburor not found in list")        

    def save_new_user(self):
        self.page.wait_for_selector(self.SAVE_BUTTON).click()    

    def cancel_user_creating(self):
        self.page.wait_for_selector(self.CANCEL_BUTTON).click()   

    def close_new_user_form(self):
        self.page.wait_for_selector(self.CLOSE_ICON).click()       

    