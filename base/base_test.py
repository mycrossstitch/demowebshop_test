import pytest
from config.data import Data
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage

class BaseTest:
    data : Data
    login_page: LoginPage
    customer_page: CustomerPage
    main_page: MainPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.customer_page = CustomerPage(driver)
        request.cls.main_page = MainPage(driver)



