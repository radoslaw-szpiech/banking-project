from playwright.sync_api import Page


class OpenAccount:
    def __init__(self, page: Page):
        self.page = page
        self.customer = self.page.locator("#userSelect")
        self.currency = self.page.locator("#currency")
        self.process_button = self.page.locator("button[type=submit]")
