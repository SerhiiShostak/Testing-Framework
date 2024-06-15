from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class RozetkaMainPage(BasePage):
    URL = "https://rozetka.com.ua"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(RozetkaMainPage.URL)

    def search_product(self, search_request):
        """
        Returns "result for [search_request]" string, if search_request isn't catalog name
        Otherwise, opens [search_request] catalog page and returns the tab name
        """
        search_field = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.NAME, "search")
                        )
        )
        search_field.send_keys(search_request)

        search_button = self.driver.find_element(
            By.CLASS_NAME,
            "button.button_color_green.button_size_medium.search-form__submit"
        )
        search_button.click()

        try:
            result_string = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located(
                                (By.CLASS_NAME, "search-heading.ng-star-inserted")
                            )
            )
            return result_string.text
        except TimeoutException:
            return self.driver.title
