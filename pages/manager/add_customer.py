from playwright.sync_api import Page


class AddCustomer:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = self.page.locator("[ng-model=fName]")
        self.last_name = self.page.locator("[ng-model=lName]")
        self.post_code = self.page.locator("[ng-model=postCd]")
        self.submit = self.page.locator("button[type=submit]")
