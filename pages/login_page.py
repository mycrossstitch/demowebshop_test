import allure

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC




class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    EMAIL_FIELD = (By.ID, "Email")
    PASSWORD_FIELD = (By.ID, "Password")
    REMEMBER_ME_CHECKBOX = (By.ID, "RememberMe")
    SUBMIT_BUTTON = (By.CLASS_NAME, "login-button")

    def enter_email(self, email):
        with allure.step("Email is entered"):
            self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(email)

    def enter_password(self, password):
        with allure.step("Password is entered"):
            self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click on 'Log in' button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()








