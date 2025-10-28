import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    ''' HEADER LOCATORS '''
    LOGO_LINK = (By.XPATH, "//img[@alt='Tricentis Demo Web Shop']")
    REGISTER_LINK = (By.CSS_SELECTOR, ".header-links .ico-register")
    LOGIN_LINK = (By.CSS_SELECTOR, ".ico-login")
    CART_LINK = (By.CSS_SELECTOR, ".ico-cart .cart-label")
    WISHLIST_LINK = (By.CSS_SELECTOR, ".header-links .ico-wishlist")
    HEADER_ACCOUNT_LINK = (By.CSS_SELECTOR, ".header-links .account")
    LOG_OUT_LINK = (By.CSS_SELECTOR, ".header-links .ico-logout")

    ''' FOOTER LOCATORS '''
    FOOTER_ACCOUNT_LINK = (By.CSS_SELECTOR, ".footer .account")

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
            )

    def open(self):
        with allure.step(f"Open page {self.PAGE_URL}"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def click_logo(self):
        with allure.step("Click on 'logo' link"):
            self.wait.until(EC.element_to_be_clickable(self.LOGO_LINK)).click()

    def click_register(self):
        with allure.step("Click on 'register' link"):
            self.wait.until(EC.element_to_be_clickable(self.REGISTER_LINK)).click()

    def click_login(self):
        with allure.step("Click on 'login' link"):
            self.wait.until(EC.element_to_be_clickable(self.LOGIN_LINK)).click()

    def click_cart(self):
        with allure.step("Click on 'cart' link"):
            self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()

    def click_wishlist(self):
        with allure.step("Click on 'wishlist' link"):
            self.wait.until(EC.element_to_be_clickable(self.WISHLIST_LINK))

    def is_logged_in(self):
        with allure.step("Logged in"):
            self.wait.until(EC.element_to_be_clickable(self.HEADER_ACCOUNT_LINK))

    def click_my_account(self):
        with allure.step("Click on 'my account' link"):
            self.wait.until(EC.element_to_be_clickable(self.HEADER_ACCOUNT_LINK)).click()








