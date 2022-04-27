from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

EXP_OPTIONS = ('excludeSwitches', ['enable-logging'])


class WebDriver:

    class __WebDriver:

        def __init__(self):
            options = Options()
            options.add_experimental_option(*EXP_OPTIONS)
            chrome_service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=chrome_service,
                                           options=options)

    driver = None

    def __init__(self):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver().driver
