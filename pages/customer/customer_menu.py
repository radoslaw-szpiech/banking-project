import re
from playwright.sync_api import Page


class CustomerMenu:
    def __init__(self, page: Page):
        self.page = page
        self.balance = self.page.locator(".center .ng-binding").nth(1)
        self.deposit_button = self.page.locator("[ng-click='deposit()']")
        self.withdrawal_button = self.page.locator("[ng-click='withdrawl()']")
        self.message = self.page.locator("[ng-show='message']")
        self.amount = self.page.get_by_placeholder("amount")
        self.process_button = self.page.locator("button[type=submit]")

    def deposit(self, amount: int):
        self.deposit_button.click()
        self.amount.fill(str(amount))
        self.process_button.click()

    def withdraw(self, amount: int):
        self.withdrawal_button.click()
        self.amount.fill(str(amount))
        self.process_button.click()
