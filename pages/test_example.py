#from I2G.pages.base_page import Base_page
from I2G.pages.login import Login_page
from playwright.sync_api import Playwright, sync_playwright, expect
from I2G.pages.base_page import Base_page
from I2G.pages.user import User_page
#from I2G.pages.user_add import Add_user_page
from I2G.helpers.user_helpers import new_user
base_url = "https://manager.idis.qa.sktelemed.net"

def test_Doctor_can_login_with_valid_credentials(page, page2, new_user):
    base_page = Base_page(page)
    base_page.open("/")
    user_page = User_page(page2)
    user_page.open("/")
    user_page.page.pause()


    login_page = Login_page(page)
    login_page.open("https://manager.idis.qa.sktelemed.net")
    

    login_page.login_user("john_snow@mailinator.com", "Idisov147")
    expect(page.get_by_role('button', name='john_snow@mailinator.com')).to_be_enabled()
    assert login_page.get_user() == 'john_snow@mailinator.com', 'No user in header'
    expect(page).to_have_url(base_url + '/')
