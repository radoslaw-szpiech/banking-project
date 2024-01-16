from playwright.sync_api import Page


class ManagerMenu:
    def __init__(self, page: Page):
        self.page = page
        self.add_customer = self.page.locator("[ng-class=btnClass1]")
        self.open_account = self.page.locator("[ng-class=btnClass2]")
        self.customers = self.page.locator("[ng-class=btnClass3]")
