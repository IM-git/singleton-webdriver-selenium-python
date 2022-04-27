import time

from base_page import BasePage

URL4 = 'https://selenium-python.readthedocs.io/locating-elements.html'
URL5 = 'https://selenium-python.readthedocs.io/waits.html'


def test_page_four(browser):
    main_page = BasePage(URL4)
    main_page.open()
    time.sleep(1)


def test_page_five(browser):
    main_page = BasePage(URL5)
    main_page.open()
    time.sleep(1)
