from pages.base_page import Base_page
from pages.login import Login_page
from playwright.sync_api import Playwright, sync_playwright, expect
from pages.base_page import Base_page
from pages.user import User_page
#from I2G.pages.user_add import Add_user_page
from helpers.user_helpers import new_user
base_url = "https://manager.idis.qa.sktelemed.net"

def test_Doctor_can_login_with_valid_credentials(app_page):
    page = app_page
    login_page = Login_page(page)
    login_page.open("/")
    # login_page.open("https://manager.idis.qa.sktelemed.net")
    
    login_page.login_user("john_snow@mailinator.com", "Idisov147")
    expect(page.get_by_role('button', name='john_snow@mailinator.com')).to_be_enabled()
    assert login_page.get_user() == 'john_snow@mailinator.com', 'No user in header'
    expect(page).to_have_url(base_url + '/')

def test_Doctor_login(desktop_app_auth_doctor):
    page = desktop_app_auth_doctor
    base_page = Base_page(page)
    base_page.open("/")
    expect(page.get_by_role('button', name='john_snow@mailinator.com')).to_be_enabled()
    assert base_page.get_user() == 'john_snow@mailinator.com', 'No user in header'
    expect(page).to_have_url(base_url + '/')
    base_page.page.pause()

