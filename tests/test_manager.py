import pytest
from playwright.sync_api import Page, Browser, expect
from pages.manager.manager_menu import ManagerMenu
from pages.manager.add_customer import AddCustomer
from pages.manager.open_account import OpenAccount
from pages.manager.customers import Customers
from pages.login import Login


url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

data = {
    "first_name": "Sirius",
    "last_name": "Black",
    "post_code": "123456",
}


@pytest.fixture(scope="module")
def page(browser: Browser):
    page = browser.new_page()
    login = Login(page)

    page.goto(url)
    login.manager_login()

    yield page
    page.close()


def test_add_customer(page: Page):
    manager_menu = ManagerMenu(page)
    add_customer = AddCustomer(page)

    manager_menu.add_customer.click()

    add_customer.first_name.fill(data["first_name"])
    add_customer.last_name.fill(data["last_name"])
    add_customer.post_code.fill(data["post_code"])
    add_customer.submit.click()


def test_open_account(page: Page):
    manager_menu = ManagerMenu(page)
    open_account = OpenAccount(page)

    manager_menu.open_account.click()

    open_account.customer.select_option(
        "%s %s" % (data["first_name"], data["last_name"])
    )
    open_account.currency.select_option("Pound")
    open_account.process_button.click()


def test_search_customer(page: Page):
    manager_menu = ManagerMenu(page)
    customers = Customers(page)

    manager_menu.customers.click()

    customers.search.fill(data["first_name"])
    expect(customers.rows).to_have_count(1)

    for key, value in data.items():
        expect(customers.rows).to_contain_text(value)


def test_delete_customer(page: Page):
    customers = Customers(page)

    customers.delete.click()
    expect(customers.rows).not_to_be_visible()
