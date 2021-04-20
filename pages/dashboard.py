"""
DashboardPage class
"""
from selenium.webdriver.common.by import By


class DashboardPage:

    # Locator
    dashboard = (By.LINK_TEXT,'Dashboard')

    def __init__(self,browser):
        self.browser = browser

    def verify_successful_login(self):
        # TODO
        pass

