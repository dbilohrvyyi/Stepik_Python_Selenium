'''
Fixtures Returning Value. We create fixture browser which creates object WebDriver and then use it in tests.

In details, we create method browser and set it with decorator @pytest.fixture.
Then we can call fixture as a parameter. By default it will be created for the each test.

Please note, we don't use browser.quit() in this example. It is not a best practice but serves as an example
that anyway it will be closed automatically by build-it fixture garbage collector.

P.S. to run use this command: pytest -s -v test_fixture2.py
'''

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")