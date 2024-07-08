from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.ui.page_object.orangehrm.orangehrm_login_page import OrangeHRMLoginPage
import os


class OrangeHRMJobTitlesPage(OrangeHRMLoginPage):
    URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList'

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(OrangeHRMJobTitlesPage.URL)
        if self.driver.current_url != OrangeHRMJobTitlesPage.URL:
            self.try_to_login()
            self.driver.get(OrangeHRMJobTitlesPage.URL)

    def change_profile_name(self, first_name, middle_name, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, 'middleName')
            )
        )

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

    def add_job_title(self, title='test_title', description='test_desc', notes='test_notes',
                      spec_file='/tests/test_files/job_title_specification.txt'):
        add_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-button.oxd-button--medium.oxd-button--secondary")))
        add_button.click()

        job_title_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'oxd-input.oxd-input--active')))[1]

        job_title_field.send_keys(title)

        text_area_list = self.driver.find_elements(
            By.CLASS_NAME, 'oxd-textarea.oxd-textarea--active.oxd-textarea--resize-vertical'
        )

        job_description_field = text_area_list[0]
        job_description_field.send_keys(description)

        note_field = text_area_list[1]
        note_field.send_keys(notes)

        upload_file_button = self.driver.find_element(By.CLASS_NAME, 'oxd-file-input')

        spec_file_dir = os.path.abspath(os.getcwd() + spec_file)
        upload_file_button.send_keys(spec_file_dir)

        save_button = self.driver.find_element(
            By.CLASS_NAME,
            'oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space'
        )
        save_button.click()

    def check_job(self, title_to_find):
        jobs_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "oxd-table-card.--mobile")
            )
        )

        for title in jobs_list:
            if title_to_find.lower() in title.text.lower():
                return title

        return False

    def delete_job(self, title_to_delete):
        deletion_job = self.check_job(title_to_delete)
        if deletion_job:
            delete_button = deletion_job.find_element(By.CLASS_NAME, 'oxd-icon-button.oxd-table-cell-action-space')
            delete_button.click()

            delete_popup_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME,
                     "oxd-button.oxd-button--medium.oxd-button--label-danger.orangehrm-button-margin"
                     )
                )
            )
            delete_popup_button.click()
