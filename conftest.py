import pytest

from browser import WebDriver

TIME = 5


@pytest.fixture(scope='session')
def browser():
    """Simple pre-initialization the Chrome webdriver
    with Singleton."""
    driver = WebDriver().driver
    driver.implicitly_wait(TIME)
    driver.maximize_window()
    yield driver
    driver.delete_all_cookies()
    driver.quit()
