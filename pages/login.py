from playwright.sync_api import Page


class Login:
    def __init__(self, page: Page):
        self.page = page
        self.customer_button = self.page.locator("[ng-click='customer()']")
        self.manager_button = self.page.locator("[ng-click='manager()']")
        self.name_selector = self.page.locator("#userSelect")
        self.login_button = self.page.locator("[type='submit']")

    def customer_login(self, name: str):
        self.customer_button.click()
        self.name_selector.select_option(label=name)
        self.login_button.click()

    def manager_login(self):
        self.manager_button.click()
