import time

from base_page import BasePage

URL1 = 'https://selenium-python.readthedocs.io/installation.html'
URL2 = 'https://selenium-python.readthedocs.io/getting-started.html'
URL3 = 'https://selenium-python.readthedocs.io/navigating.html'


def test_page_one(browser):
    main_page = BasePage(URL1)
    main_page.open()
    time.sleep(1)


def test_page_two(browser):
    main_page = BasePage(URL2)
    main_page.open()
    time.sleep(1)


def test_page_three(browser):
    main_page = BasePage(URL3)
    main_page.open()
    time.sleep(1)
