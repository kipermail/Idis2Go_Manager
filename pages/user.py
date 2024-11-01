from playwright.sync_api import Page
from pages.base_page import Base_page
#from I2G.pages.base_page import Base_page
from helpers.user_helpers import UserColumns, UserFilters

class User_page(Base_page):
    
    PAGE_URL =  "/user/"

    
    ADD_BUTTON = ('.content-heading >> a[href="/user/add/"]')
    COLUMNS = ('.panel-header >> a[data-target="#ModalColumn"]')
    FILTERS = ('a[data-target="#ModalFilter"]')
    FILTERS_IS_ON = ('.table-filter-active')
    SEARCH_FIELD = ('.panel-header >> input[name="search"]')

    IS_STAFF_COLUMN = ('table#result_list th#column_is_staff')

    # CHECK_COLUMN_EMAIL = ('id="setup_dialog_base_user_table" input[value="email"]')
    # CHECK_COLUMN_EMAIL_VERIFIED = ('id="setup_dialog_base_user_table" input[value="email_verified"]')
    # CHECK_COLUMN_FIRST_NAME = ('id="setup_dialog_base_user_table" input[value="first_name"]')
    # CHECK_COLUMN_LAST_NAME = ('id="setup_dialog_base_user_table" input[value="last_name"]')
    # CHECK_COLUMN_ROLE = ('id="setup_dialog_base_user_table" input[value="role"]')
    # CHECK_COLUMN_DISTRIBUTOR = ('id="setup_dialog_base_user_table" input[value="distributor"]')
    # CHECK_COLUMN_IS_STAFF = ('id="setup_dialog_base_user_table" input[value="is_staff"]')
    # CHECK_COLUMN_IS_SUPERUSER = ('id="setup_dialog_base_user_table" input[value="is_superuser"]')
    # CHECK_COLUMN_IS_DOCTOR = ('id="setup_dialog_base_user_table" input[value="is_doctor"]')
    # CHECK_COLUMN_ACTIONS = ('id="setup_dialog_base_user_table" input[value="actions"]')


    def __init__(self, page: Page):
        self.page = page
        self.columns = UserColumns(page)
        self.filters = UserFilters(page)

    def add_new_user(self):
        self.page.wait_for_selector(self.ADD_BUTTON).click()
        self.page.wait_for_load_state()



    def search_user(self, search_string: str):
        self.page.wait_for_selector(self.SEARCH_FIELD).fill(search_string)
        self.page.wait_for_selector(self.SEARCH_FIELD).press("Enter")
        rows = self.page.locator('table#result_list tbody tr:has(td:has-text("Kirill"))')
        print(rows.count())

    def open_userlist_columns(self):
        self.page.wait_for_selector(self.COLUMNS)
        self.page.locator(self.COLUMNS).click()
        self.page.wait_for_load_state()

    def open_userlist_filters(self):
        self.page.wait_for_selector(self.FILTERS)
        self.page.locator(self.FILTERS).click()
        self.page.wait_for_load_state()

    def is_column_displayed(self, column):
        selector = f'table#result_list th#column_{column}'
        self.page.wait_for_selector(selector, timeout=5000)
        return self.page.locator(selector).is_visible()
    
    def is_column_not_displayed(self, column):
        selector = f'table#result_list th#column_{column}'
        return self.page.locator(selector).is_hidden(timeout=5000)
    
    def is_filters_on(self):
        self.page.wait_for_load_state()
        return self.page.locator(self.FILTERS_IS_ON).is_visible()

    def is_filters_off(self):
        self.page.wait_for_load_state()
        return self.page.locator(self.FILTERS_IS_ON).is_hidden()

    