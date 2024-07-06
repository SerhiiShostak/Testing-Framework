from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import options


class OrangeHRMLoginPage(BasePage):
    URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    DEMO_USERNAME = 'Admin'
    DEMO_PASSWORD = 'admin123'

    def __init__(self):
        super().__init__(options)

    def go_to(self):
        self.driver.get(OrangeHRMLoginPage.URL)

    def login_webdriver(self):
        return self.driver

    def try_to_login(self):
        username_input = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys(OrangeHRMLoginPage.DEMO_USERNAME)

        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(OrangeHRMLoginPage.DEMO_PASSWORD)

        login_button = self.driver.find_element(By.TAG_NAME, 'button')
        login_button.click()

    def check_dashboard(self):
        dashboard_div = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'oxd-topbar-header-title')
            )
        )

        return dashboard_div
