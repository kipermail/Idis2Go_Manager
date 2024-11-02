import os
import json
import pytest
import logging
import allure
from pytest import fixture
from faker import Faker
# I2G.models.user import User  
from playwright.sync_api import sync_playwright, expect, Request
from pages.app import App
from pages.login import Login_page
from pages.base_page import Base_page


# @fixture(scope='session')
# def get_browser():
#     with sync_playwright() as playw:
#         brow = playw.chromium.launch(headless=False)
#         yield brow
#         brow.close()

#@fixture(scope='session', params=['chromium'])
@fixture(scope='session')
def get_browser(request):
    with sync_playwright() as playw:
        #browser = request.param
        browser = request.config.getoption('--dbrowser')
        headless = request.config.getini('headless')
        if headless == 'True':
            headless = True
        else:
            headless = False
        if browser == 'chromium':
            brow = playw.chromium.launch(headless=False, devtools=False)
#           brow = playw.chromium.launch(headless=headless, devtools=False)
        elif browser == 'firefox':
            brow = playw.firefox.launch(headless=headless)
        elif browser == 'webkit':
            brow = playw.webkit.launch(headless=headless)
        else:
            assert False, 'unsupported browser type'       
        yield brow
        brow.close()


@fixture(scope='function')
def app_page(get_browser):
    context = get_browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()

# @fixture(scope="session")
# def desktop_app(get_browser, request):
#     base_url = request.config.getini('base_url')
#     context = get_browser.new_context()
#     page = context.new_page()
#     app = App(get_browser, base_url="https://manager.idis.qa.sktelemed.net")
#     app.goto("/")
#     yield app
#     app.close()
    
    
@fixture(scope="function")
def desktop_app_auth_doctor(app_page, request):
    app = Login_page(app_page)
    app.open("/")
    base_url = request.config.getini('base_url')
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
#   app.login_page.login_user("john_snow@mailinator.com", "Idisov147")
    app.login_user(**config['users']['Manager'])
    expect(app.page.get_by_role('button', name='john_snow@mailinator.com')).to_be_enabled()
    assert app.get_user() == config['users']['Manager']['login']
    expect(app.page).to_have_url(base_url + '/') 
    yield app_page      
    

 # def __init__(self, playwright: Playwright, base_url: str, **kwargs):
    #     self.browser = playwright.chromium.launch(headless="headless", devtools="devtools")
    #     self.context = self.browser.new_context(**kwargs )
    #     self.page = self.context.new_page()
    #     self.base_url = base_url

def pytest_addoption(parser):
    parser.addoption('--secure', action='store', default='secure.json')
    parser.addoption('--dbrowser', action='store', default='chromium')
    parser.addini('base_url', help='base url of site under test', default="https://manager.idis.qa.sktelemed.net")
    parser.addini('headless', help='run browser in headless mode', default='False')


def load_config(project_path: str, file: str) -> dict:
    config_file = os.path.join(project_path, file)
    with open(config_file) as cfg:
        return json.loads(cfg.read())