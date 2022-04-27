Singleton Webdriver Selenium Python
===
___
This is simple example how use singleton with webdriver for testing.\
With this pattern can to running tests and use only one webdriver per session.\
_It is divergent in opinion the pattern. More information, to use or not, look on the internet._
___
Packages:

`selenium==4.1.3`\
`pytest==7.1.2`\
`webdriver-manager==3.5.4`
___
Singleton pattern:

    class WebDriver:
    
        class __WebDriver:
            def __init__(self):
                self.driver = webdriver.Chrome(r'C:\..\chromedriver.exe')
    
        driver = None
    
        def __init__(self):
            if not self.driver:
                WebDriver.driver = WebDriver.__WebDriver().driver
___
In the terminal shown browser-id.\
Use command `pytest -s -v`. \
Example of the response part:

        test_case_two.py::test_page_five
        ID: 1460955397376
        We're on the https://selenium-python.readthedocs.io/waits.html
        PASSED
___
###### `Python 3, version 3.10.4`