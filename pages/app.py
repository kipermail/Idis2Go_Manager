from playwright.sync_api import Playwright, sync_playwright
import argparse

class App:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.setup_arguments()



    #     self.browser = None
    #     self.context = None
    #     self.page = None

    # def start(self):
    #     with sync_playwright() as playwright:
    #         self.browser = playwright.chromium.launch(headless=False)
    #         self.context = self.browser.new_context()
    #         self.page = self.context.new_page()

    # def stop(self):
    #     if self.context:
    #         self.context.close()
    #     if self.browser:
    #         self.browser.close()



    def setup_arguments(self):
        self.parser.add_argument('--url', type=str, help='URL of the application')

    def parse(self):
        return self.parser.parse_args()
