"""
UserRegistrationPage class
"""
from selenium.webdriver.common.by import By


class UserRegistrationPage:
    # Locator
    EMAIL = (By.ID, 'reg_email')
    PASSWORD = (By.ID, 'password')
    REGISTER_BUTTON = (By.NAME, 'register')

    def __init__(self, browser):
        self.browser = browser

    def user_registration(self, email, password):
        email_object = self.browser.find_element(*self.EMAIL)
        email_object.send_Keys(email)
        password_object = self.browser.find_element(*self.PASSWORD)
        password_object.send_Keys(password)
        self.browser.find_element(*self.REGISTER_BUTTON)
