from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


class BasePage:

    def __init__(self, options=None):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

    def go_to(self):
        pass

    def get_tab_name(self):
        return self.driver.title

    def close(self):
        self.driver.close()
