from browser import WebDriver


class BasePage:

    def __init__(self, url: str):
        self.browser = None
        self.url = url

    def __browser(self):
        self.browser = WebDriver().driver
        return self.browser

    def __information(self) -> None:
        print(f"We're on the {self.url}")

    def __id_info(self) -> None:
        print(f'\nID: {id(self.browser)}')

    def open(self) -> None:
        """Performing open the page"""
        self.__browser().get(url=self.url)
        self.__id_info()
        self.__information()
