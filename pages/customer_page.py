from email.charset import add_alias

import allure

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class CustomerPage(BasePage):

    PAGE_URL = Links.CUSTOMER_INFO_PAGE

    GENDER_MALE_CHECK = (By.ID, "gender-male")
    GENDER_FEMALE_CHECK = (By.ID, "gender-female")
    FIRST_NAME_FIELD = (By.ID, "FirstName")
    LAST_NAME_FIELD = (By.ID, "LastName")
    EMAIL_FIELD = (By.ID, "Email")
    SAVE_BUTTON = (By.XPATH, "//input[@name='save-info-button']")

    def change_gender(self, gender):
        with allure.step(f"Change gender"):
            LOCATOR_GENDER = (By.ID, f"gender-{gender}")
            element = self.wait.until(EC.presence_of_element_located(LOCATOR_GENDER))
            self.driver.execute_script("arguments[0].click();", element)

    def change_first_name(self, new_first_name):
        with allure.step(f"Change first name"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            first_name_field.clear()
            first_name_field.click()
            self.driver.execute_script("arguments[0].value = arguments[1];", first_name_field, new_first_name)

    def change_last_name(self, new_last_name):
        with allure.step(f"Change last name"):
            last_name_field = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD))
            last_name_field.clear()
            last_name_field.click()
            self.driver.execute_script("arguments[0].value = arguments[1];", last_name_field, new_last_name)

    def change_email(self, new_email):
        with allure.step(f"Change email"):
            email_field = self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD))
            email_field.clear()
            email_field.click()
            self.driver.execute_script("arguments[0].value = arguments[1];", email_field, new_email)

    def save_changes (self):
        with allure.step("Save changes"):
            self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    def is_changes_saved_name(self, new_first_name):
        with allure.step("Check if first_name was saved successfully"):
            self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, new_first_name))

    def is_changes_saved_last_name(self, new_last_name):
        with allure.step("Check if last_name was saved successfully"):
            self.wait.until(EC.text_to_be_present_in_element_value(self.LAST_NAME_FIELD, new_last_name))


    def is_changes_saved_email(self, new_email):
        with allure.step("Check if email was saved successfully"):
            self.wait.until(EC.text_to_be_present_in_element_value(self.EMAIL_FIELD, new_email))

    def is_changes_saved_gender(self, new_gender):
        with allure.step("Check if gender was saved successfully"):
            if new_gender == "male":
                self.wait.until(lambda d: d.find_element(*self.GENDER_MALE_CHECK).is_selected())
            elif new_gender == "female":
                self.wait.until(lambda d: d.find_element(*self.GENDER_FEMALE_CHECK).is_selected())














