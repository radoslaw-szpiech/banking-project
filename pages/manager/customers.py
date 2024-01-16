from playwright.sync_api import Page


class Customers:
    def __init__(self, page: Page):
        self.page = page
        self.search = self.page.get_by_placeholder("Search Customer")
        self.rows = self.page.locator("tbody tr")
        self.delete = self.page.locator("tbody tr button")
