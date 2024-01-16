import pytest
from playwright.sync_api import Page, Browser, expect
from pages.login import Login
from pages.customer.customer_menu import CustomerMenu

url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"


@pytest.fixture(scope="function")
def page(browser: Browser):
    page = browser.new_page()
    page.goto(url)
    yield page
    page.close()


def test_desposit(page: Page):
    login = Login(page)
    customer_menu = CustomerMenu(page)

    login.customer_login("Harry Potter")
    customer_menu.deposit(1000)
    expect(customer_menu.message).to_have_text("Deposit Successful")
    expect(customer_menu.balance).to_have_text("1000")


def test_withdraw_success(page: Page):
    login = Login(page)
    customer_menu = CustomerMenu(page)

    login.customer_login("Hermoine Granger")
    balance = int(customer_menu.balance.text_content())
    customer_menu.withdraw(100)
    expect(customer_menu.message).to_have_text("Transaction successful")
    expect(customer_menu.balance).to_have_text(str(balance - 100))


def test_withdraw_no_funds(page: Page):
    login = Login(page)
    customer_menu = CustomerMenu(page)

    login.customer_login("Harry Potter")
    customer_menu.withdraw(1000)
    expect(customer_menu.message).to_have_text(
        "Transaction Failed. You can not withdraw amount more than the balance."
    )
