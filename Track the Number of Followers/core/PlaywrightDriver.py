from playwright.sync_api import sync_playwright
import json

class PlaywrightDriver:
    def __init__(self, cookies_file=None):
        self.cookies_file = cookies_file

    def initialize_driver(self):
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()

        if self.cookies_file:
            with open(self.cookies_file, 'r') as file:
                cookies = json.load(file)
                context.add_cookies(cookies)

        return context

    def close(self, context):
        context.close()
