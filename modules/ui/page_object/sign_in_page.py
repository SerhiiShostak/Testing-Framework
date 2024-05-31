from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_to_login(self, username, password):
        login_input = self.driver.find_element(By.ID, "login_field")
        login_input.send_keys(username)

        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(password)

        sign_in_button = self.driver.find_element(By.NAME, 'commit')
        sign_in_button.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
