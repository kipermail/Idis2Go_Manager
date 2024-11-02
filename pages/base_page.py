from playwright.sync_api import Page, expect
import pytest
#from I2G.pages.app import App
from pages.app import App

class Base_page():
    base_url = "https://manager.idis.qa.sktelemed.net"

    PAGE_URL = "/" 
    MENU_USER = ('#main-menu >> a[href="/user/"]')
    MENU_CUSTOMER = ('#main-menu >> a[href="/customer/"]')
    MENU_DISTRIBUTOR = ('#main-menu >> a[href="/distributor/"]')
    MENU_RESULT = ('#main-menu >> a[href="/result/"]')
    MENU_STATISTIC = ('#main-menu >> a[href="/statistics/"]')
    MENU_INSTALLATIONS = ('#main-menu >> a[href="#installations-block"]')
    MENU_KITS = ('a[href="/kit/"]')
    MENU_ACTIVATION = ('a[href="/device-activation/"]')
    MENU_DEVICE_SESSION = ('a[href="/device-session/"]')
    MENU_KITS_SETTINGS = ('#main-menu >> a[href="#kits-settings-block"]')
    MENU_VENDOR = ('a[href="/vendor/"]')
    MENU_TICKET = ('#main-menu >> a[href="/ticket/"]')
    MENU_UPDATE = ('#main-menu >> a[href="#update-block"]')
    MENU_SERVICE = ('#main-menu >> a[href="/service/"]')
    MENU_UPDATE = ('#main-menu >> a[href="#settings-block"]')
    NAVBAR_LOGOUT = ('.nav-wrapper >> a[href="//manager.idis.qa.sktelemed.net/logout/"]')
    NAVBAR_USER = ('.nav-wrapper >> .btn-transparent')
    NAVBAR_HOME = ('.navbar-header >> a[href="/"]')
    NAVBAR_CURRENT_LANGUAGE = ('.select2-selection__rendered')


    def __init__(self, page: Page):
        #super().__init__(page)  # Вызов __init__ родительского класса
        self.page = page
        #self.base_url = "https://manager.idis.qa.sktelemed.net"

    def open(self, endpoint: str, use_base_url=True):   
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else: 
            self.page.goto(endpoint)
    

    def navigate_to_menu(self, menu):
        self.page.wait_for_selector(menu).click()
        self.page.wait_for_load_state()   

    def navigate_to_submenu(self, menu, submenu):
        self.page.wait_for_selector(menu).click()
        self.page.wait_for_selector(submenu).click()
        self.page.wait_for_load_state()   


    def navigate_to_home(self):
        self.page.locator(self.NAVBAR_HOME).click()

    def logout(self):
        self.page.locator(self.NAVBAR_LOGOUT).click()

    def get_user(self):
        user = self.page.query_selector(self.NAVBAR_USER).inner_text()
        return user

    def change_password(current_password: str, new_password: str, confirm_password=''):
        pass

    def sign_out(self):
        pass


    def get_language(self):
        self.page.wait_for_selector(self.NAVBAR_CURRENT_LANGUAGE)
        return self.page.locator(self.NAVBAR_CURRENT_LANGUAGE).inner_text()

    def change_language(self, language: str):
        self.page.wait_for_selector('.select2-selection')
        self.page.click('.select2-selection')
        self.page.wait_for_selector('.select2-results')
        self.page.locator('li.select2-results__option').filter(has_text=language).click()

    def is_page_opened(self, page_url: str):
        return self.page.url == self.base_url + self.PAGE_URL
        #return self.page.to_have_url(self.base_url + page_url)
    

    def close(self):
        self.page.close()
        self.context.close()