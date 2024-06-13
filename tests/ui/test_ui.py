import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.ui
def test_check_incorrect_username():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    driver.get("https://github.com/login")

    login_input = driver.find_element(By.ID, "login_field")
    login_input.send_keys('wrongdata198')

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys('wrongdata198')

    sign_in_button = driver.find_element(By.NAME, 'commit')
    sign_in_button.click()

    assert driver.title == 'Sign in to GitHub · GitHub'

    driver.close()
