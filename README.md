# banking-project

A few examples of tests for https://www.globalsqa.com/angularJs-protractor/BankingProject

## Installation and run

1. Have Python installed on your machine.
2. Install pytest-playwright - `pip install pytest-playwright`
3. Install browsers - `playwright install`
4. Run test by simply running `pytest` or `pytest --headed` to have live view of tests being run.

## Overview

It's a example of simple tests using Python and Plywright. Tested app is UI only, without backend support. Tests are not fully consistent as I wanted to present different approaches of writing tests.

-   `test_customer.py` - here tests are isolated, each single test is run in fresh browser instance, so there is no risk that any action or data from one test affects other ones. Page Object model was used to cover repetitive actions (deposit, withdraw) and locators usage.
-   `test_manager.py`- in this case there is a single flow in single browser instance. Each test is in fact single step of customer CRUD, data that is created in application is then used in later steps. Simplified POM approach is used - objects contain locators only, all actions are explicitly taken in test script itself. This kind of approach can be used, when we preffer better "code visibility" and making it easier to debug, but we accept the risk of repetitive code and maintability issues in more complex scenarios.

Few things could be added (besides more test cases):

-   data preperation - there is no backend or DB, that can be mocked, but as all data is kept in local storage, we could inject all data we need for specific test (users, accounts, balance, etc.).
-   fail fast - in `test_manager.py` - if any step fails, all other tests will fail as well, but playwright still tries to run them. Some logic could be added to skip further tests if any previous tests fails.
-   global config - some summary settings of the project, like url, timeouts, fixtures could be gathered and shared among all tests cases.
