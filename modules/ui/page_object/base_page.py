from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


class BasePage:

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    def __init__(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=BasePage.options
        )

    def close(self):
        self.driver.close()
