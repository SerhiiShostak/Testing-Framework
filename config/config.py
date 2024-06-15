from selenium import webdriver

# Headless parameter uses for GitHub Actions
options = webdriver.ChromeOptions()
options.add_argument('headless')
