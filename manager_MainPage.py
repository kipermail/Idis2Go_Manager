from playwright.sync_api import Playwright, sync_playwright, expect
from pages.login import Login_page
from pages.base_page import Base_page
from pages.user import User_page
from pages.user_add import Add_user_page
#from helpers.user_helpers import UserColumns, UserFilters


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    base_url = "https://manager.idis.qa.sktelemed.net"
    #page.goto(base_url)
    login_page = Login_page(page)
    base_page = Base_page(page)
    user_page = User_page(page)
    add_user_page = Add_user_page(page)
    base_page.open("/")
    login_page.login_user("john_snow@mailinator.com", "Idisov147")
    expect(page.get_by_role('button', name='john_snow@mailinator.com')).to_be_enabled()
    assert base_page.get_user() == 'john_snow@mailinator.com'
    expect(page).to_have_url(base_url + '/')
    menu_user = page.locator('#main-menu >> a[href="/user/"]').click()
    page.wait_for_timeout(500)
    assert page.url == base_url + '/user/'
    #     #user_page.search_user("Kirill")
    user_page.open_userlist_columns()
    #columns = UserColumns()
    current_columns = user_page.columns.get_columns_state()
    active_fields = ['is_staff', 'role' ]
    user_page.columns.set_columns_state(active_fields)
    user_page.columns.enable_checkbox('role')
    user_page.columns.save_columns_form()
    user_page.open_userlist_columns()
    user_page.columns.enable_checkbox('is_doctor')
    user_page.columns.close_columns_form()
    assert user_page.is_column_displayed('is_staff'), "is_staff error"
    assert user_page.is_column_not_displayed('customer'), "customer error"
    user_page.open_userlist_filters()
    #filters = UserFilters(page)
    user_page.filters.set_filter_state("is_archive", "yes")
    user_page.filters.set_filter_multiple_state("roles", ["Superuser", "Regional manager"]) #"Regional manager"

    user_page.filters.applay_filters_form()
    assert user_page.is_filters_on(), "Filter not set ON"
    #assert user_page.is_filters_off(), "Filter not set OFF"


    # user_page.set_userlist_filters()
    base_page.navigate_to_menu(base_page.MENU_CUSTOMER)
    #menu_customer = page.locator('#main-menu >> a[href="/customer/"]').click()
    page.wait_for_timeout(500)
    assert page.url == base_url + '/customer/'
    menu_distributor = page.locator('#main-menu >> a[href="/distributor/"]').click()
    page.wait_for_timeout(500)
    assert page.url == base_url + '/distributor/'
    menu_result = page.locator('#main-menu >> a[href="/result/"]').click()
    page.wait_for_timeout(500)
    user_page.open_userlist_filters()
    user_page.filters.set_filter_date_state("start_date", "2024-10-20")
    user_page.filters.set_filter_date_state("end_date", "2024-10-20")
    menu_statistics = page.locator('#main-menu >> a[href="/statistics/"]').click()
    
    base_page.navigate_to_submenu(base_page.MENU_INSTALLATIONS, base_page.MENU_ACTIVATION)
    
    base_page.navigate_to_home()
    page.wait_for_load_state()
    expect(page).to_have_url(base_url + "/")

    base_page.change_language("RU")
    page.wait_for_timeout(500)
    assert base_page.get_language() == "RU"
    base_page.logout()
    # navbar_logout = page.locator('.nav-wrapper >> a[href="//manager.idis.qa.sktelemed.net/logout/"]')
    # navbar_logout.click()
    page.wait_for_load_state()
    assert login_page.is_page_opened('')
    #expect(page).to_have_url(base_url + "/login/")

    

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


    # ----образцы вызовов для формы нового пользователя----
    #user_page.add_new_user()
    # add_user_page.enter_first_name("Dima_1")
    # add_user_page.enter_last_name("Gol_1")
    # add_user_page.enter_email("dima@email.com")
    # add_user_page.enter_password("Ivanov148")
    
    # add_user_page.select_language("RU")
    # add_user_page.select_role('Distributor administrator')
    # add_user_page.select_distributor('DEMO')

    # add_user_page.select_email_verified(False)
    # add_user_page.select_is_active(True)
    # #add_user_page.select_is_doctor(True)
    # #assert add_user_page.is_doctor_visible()

    # # user_page.add_new_user()
    # # user_page.enter_first_name(new_user.first_name)
    # # user_page.enter_last_name(new_user.last_name)
    # # user_page.enter_email(new_user.email)
    # # user_page.enter_password(new_user.password)
    # # user_page.select_language(new_user.language)
    # # user_page.select_role(new_user.role)
    # # user_page.select_distributor(new_user.distributor)
    # # user_page.select_email_verified(new_user.email_verified)
    # # user_page.select_is_active(new_user.is_active)
    # # user_page.select_is_doctor(new_user.is_doctor)
    # #add_user_page.close_new_user_form()
    # add_user_page.cancel_user_creating()

    # ----образцы вызовов для перехода в меню----
    # page.goto("https://manager.idis.qa.sktelemed.net/user/")
    # page.goto("https://manager.idis.qa.sktelemed.net/customer/")
    # page.goto("https://manager.idis.qa.sktelemed.net/distributor/")
    # page.goto("https://manager.idis.qa.sktelemed.net/result/")
    # page.goto("https://manager.idis.qa.sktelemed.net/statistics/")
    # page.goto("https://manager.idis.qa.sktelemed.net/ticket/")
    # page.goto("https://manager.idis.qa.sktelemed.net/service/")
    # page.goto("https://manager.idis.qa.sktelemed.net/user/")
    #page.wait_for_timeout(500) 
    # assert page.url == base_url + '/statistics/'
    # menu_installations = page.locator('#main-menu >> a[href="#installations-block"]')
    # menu_installations.click()
    # assert menu_installations.locator('a[href="/kit/"]').is_visible
    # assert menu_installations.locator('a[href="/device-activation/"]').is_visible
    # assert menu_installations.locator('a[href="/device-session/"]').is_visible
    # menu_kits_settings = page.locator('#main-menu >> a[href="#kits-settings-block"]')
    # menu_kits_settings.click()
    # page.wait_for_timeout(500) 
    # assert menu_kits_settings.locator('a[href="/vendor/"]').is_visible

    # menu_ticket = page.locator('#main-menu >> a[href="/ticket/"]').click()
    # page.wait_for_timeout(500) 
    #assert page.url == base_url + '/ticket/'
    # expect(page).to_have_url(base_url + '/ticket/')
    # menu_update = page.locator('#main-menu >> a[href="#update-block"]')
    # menu_update.click()
    # menu_service = page.locator('#main-menu >> a[href="/service/"]').click()
    # page.wait_for_timeout(500) 
    # #assert page.url == base_url + '/service/'
    # expect(page).to_have_url(base_url + '/service/')
    # menu_update = page.locator('#main-menu >> a[href="#settings-block"]')
    # menu_update.click()
    # navbar_logo = page.locator('.navbar-header >> a[href="/"]')
    # navbar_logo.click()

    #---- образцы логина и смена языка ----
    # page.goto("https://manager.idis.qa.sktelemed.net/login/")
    # page.get_by_role("button", name="john_snow@mailinator.com").click()
    # page.get_by_role("link", name="Change password").click()
    # page.locator("#changePass").get_by_label("Close").click()
    # page.get_by_title("EN\n      ").click()
    # page.goto("https://manager.idis.qa.sktelemed.net/user/")

    # page.wait_for_selector('.select2-selection')
    # page.click('.select2-selection')
    # page.wait_for_selector('.select2-results')
    # page.click('li.select2-results__option:has-text("UA")')  
    # page.wait_for_selector('.select2-selection__rendered')
    # page.wait_for_timeout(500)
    # expect(page.locator('.select2-selection__rendered')).to_have_text('UA')

    