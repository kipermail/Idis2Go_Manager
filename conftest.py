import pytest
from faker import Faker
from I2G.models.user import User  
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as playw:
        browser = playw.chromium.launch(headless=False, devtools=False)
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope='function')
def page2(browser):
    context = browser.new_context()
    page2 = context.new_page()
    yield page2
    page2.close()

 # def __init__(self, playwright: Playwright, base_url: str, **kwargs):
    #     self.browser = playwright.chromium.launch(headless="headless", devtools="devtools")
    #     self.context = self.browser.new_context(**kwargs )
    #     self.page = self.context.new_page()
    #     self.base_url = base_url

