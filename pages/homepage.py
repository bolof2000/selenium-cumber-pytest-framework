"""
HomePage Class Implementation
"""
from selenium.webdriver.common.by import By


class LaunchHomePage:

    URL = "https://duckduckgo.com/"
    MY_ACCOUNT = (By.LINK_TEXT,'My account')

    def __init__(self, browser):
        self.browser = browser

    def launch_url(self):
        self.browser.get(self.URL)

    def navigate_to_register_page(self):
        self.browser.find_element(*self.MY_ACCOUNT).click()