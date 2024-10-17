# test_login.py
import time
from multiprocessing.util import LOGGER_NAME

from utilities.read_properties import Read_Config
from base_pages.Login_Admin_Page import LoginAdminPage
from utilities.loggers import  log_maker
class TestLoginAdmin:
    # Reading values from the config file
    blazedemo_URL = Read_Config.get_admin_page_url()
    username = Read_Config.get_valid_username()
    password = Read_Config.get_valid_password()
    invalidUsername = Read_Config.get_invalid_username()
    invalidPassword = Read_Config.get_invalid_password()
    logger = log_maker.log_gen()

    def test_title_verification(self, setup):
        self.logger.info("Verification of Launching page title")
        driver = setup
        driver.get(self.blazedemo_URL)
        time.sleep(3)
        actual_title = driver.title
        expected_title = 'STORE'
        assert actual_title == expected_title, f"Expected title: {expected_title}, but got: {actual_title}"
        self.logger.info("Launching page title matched as expected")

    def test_valid_admin_login(self, setup):
        self.logger.info("Verification of valid admin login")
        driver = setup
        driver.get(self.blazedemo_URL)

        login_page = LoginAdminPage(driver)
        login_page.click_login_optn()
        time.sleep(3)
        login_page.enter_username(self.username)
        login_page.enter_password(self.password)
        login_page.click_login_btn()
        time.sleep(3)
        self.logger.info("user login successfully")
        # Verify if the welcome text appears with the correct username
        welcome_text = login_page.get_welcome_text()
        expected_welcome_text = f"Welcome {self.username}"
        assert welcome_text == expected_welcome_text, f"Expected '{expected_welcome_text}', but got '{welcome_text}'"
        time.sleep(3)
        self.logger.info("welcome text is visible as expected")
        login_page.click_logout_optn()
        self.logger.info("Logout from application")
    def test_invalid_admin_login(self, setup):
        self.logger.info("Verification of invalid login")
        driver = setup
        driver.get(self.blazedemo_URL)

        login_page = LoginAdminPage(driver)
        login_page.click_login_optn()
        time.sleep(3)
        login_page.enter_username(self.invalidUsername)
        login_page.enter_password(self.invalidPassword)
        login_page.click_login_btn()
        self.logger.info("Trying to login with invalid credentials")
        time.sleep(3)
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        self.logger.info("Handling error Message alert")

