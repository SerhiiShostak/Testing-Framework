from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RozetkaLaptopsPage(BasePage):
    URL = "https://rozetka.com.ua/ua/notebooks/c80004/"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(RozetkaLaptopsPage.URL)

    def get_laptop_name_from_page(self):
        """Returns name of the first laptop on the page"""
        laptop_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'goods-tile__title')
            )
        ).text

        return laptop_name

    def try_to_add_laptop_to_cart(self):
        """Adds the first laptop to cart"""
        add_to_cart_button_first_laptop = self.driver.find_element(
            By.CLASS_NAME,
            'buy-button.goods-tile__buy-button.ng-star-inserted'
        )
        add_to_cart_button_first_laptop.click()

    def open_cart(self):
        """Opens cart modal window"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "badge.badge--green.ng-star-inserted")
            )
        )
        open_cart_button = self.driver.find_element(
            By.XPATH,
            '/html/body/rz-app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[8]/rz-header-cart/button'
        )
        open_cart_button.click()

    def get_laptop_name_from_cart(self):
        """Returns name of the first laptop in the cart"""
        laptop_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/rz-app-root/rz-single-modal-window/div[3]/"
                 "div[2]/rz-shopping-cart/div/rz-cart-purchases/ul/li/"
                 "rz-cart-product/div/div[1]/div[2]/rz-button-product-page/a/span"
                 )
            )
        ).text

        return laptop_name

    def try_to_delete_from_cart(self):
        """Removes the first laptop from the cart and checks the message about empty cart"""
        delete_from_cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'button.button--white.button--small.popup-menu__toggle.popup-menu__toggle--context')
            )
        )
        delete_from_cart_button.click()

        delete_from_cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'button.button--medium.button--with-icon.button--link')
            )
        )
        delete_from_cart_button.click()

        empty_cart_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CLASS_NAME, 'cart-dummy__heading'))).text

        return empty_cart_message == 'Кошик порожній'

    def check_name_of_laptop(self):
        """Compares name of the first laptop on the page and name of the laptop in the cart"""
        return self.get_laptop_name_from_page() == self.get_laptop_name_from_cart()
