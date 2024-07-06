from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.ui.page_object.orangehrm.orangehrm_login_page import OrangeHRMLoginPage
from selenium.webdriver import Keys


class OrangeHRMProfilePage(OrangeHRMLoginPage):
    URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7'

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(OrangeHRMProfilePage.URL)
        if self.driver.current_url != OrangeHRMProfilePage.URL:
            self.try_to_login()
            self.driver.get(OrangeHRMProfilePage.URL)

    def change_profile_name(self, first_name, middle_name, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, 'middleName')
            )
        )

        middle_name_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.NAME, 'middleName')
            )
        )

        middle_name_field.click()
        middle_name_field.send_keys(Keys.CONTROL + "a")
        middle_name_field.send_keys(Keys.DELETE)
        middle_name_field.send_keys(middle_name)

        first_name_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.NAME,
                 'firstName')
            )
        )
        first_name_field.send_keys(Keys.CONTROL + "a")
        first_name_field.send_keys(Keys.DELETE)
        first_name_field.send_keys(first_name)

        last_name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, 'lastName')
            )
        )

        last_name_field.send_keys(Keys.CONTROL + "a")
        last_name_field.send_keys(Keys.DELETE)
        last_name_field.send_keys(last_name)

        submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > '
                    'div > div > div > div.orangehrm-edit-employee-content > '
                    'div.orangehrm-horizontal-padding.orangehrm-vertical-padding > form > div.oxd-form-actions > button'
                )
            )
        )

        submit_button.click()

    def get_profile_name(self):
        profile_name_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'oxd-userdropdown-name'))
        )

        profile_name = profile_name_element.text

        return profile_name
