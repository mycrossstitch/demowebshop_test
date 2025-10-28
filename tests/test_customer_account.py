import allure
import pytest

from base.base_test import BaseTest


@allure.feature("Test Customer Account")
class TestCustomerAccount(BaseTest):

    @allure.title("Test Login")
    @allure.severity("CRITICAL")
    @pytest.mark.smoke
    def test_login(self):
        self.login_page.open()
        self.login_page.enter_email(self.data.EMAIL)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.login_page.is_logged_in()
        self.customer_page.make_screenshot("after_login")

    @allure.title("Change account details")
    @allure.severity("CRITICAL")
    @pytest.mark.ui
    def test_changes_name(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_email(self.data.EMAIL)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.login_page.is_logged_in()
        self.login_page.click_my_account()
        self.customer_page.is_opened()
        self.customer_page.change_gender(self.data.NEW_GENDER)
        self.customer_page.change_first_name(self.data.NEW_FIRST_NAME)
        self.customer_page.change_last_name(self.data.NEW_LAST_NAME)
        self.customer_page.change_email(self.data.NEW_EMAIL)
        self.customer_page.save_changes()
        self.customer_page.is_changes_saved_gender(self.data.NEW_GENDER)
        self.customer_page.is_changes_saved_name(self.data.NEW_FIRST_NAME)
        self.customer_page.is_changes_saved_last_name(self.data.NEW_LAST_NAME)
        self.customer_page.is_changes_saved_email(self.data.NEW_EMAIL)




