from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginAdminPage:
    login_option_id='login2'
    username_field_id='loginusername'
    password_field_id='loginpassword'
    login_btn_xpath='//button[@onclick="logIn()"]'
    welcome_text_id='nameofuser'
    logout_option_id='logout2'



    def __init__(self,driver):
        self.driver=driver
    def click_login_optn(self):
        self.driver.find_element(By.ID, self.login_option_id).click()

    def enter_username(self,username):
        self.driver.find_element(By.ID, self.username_field_id).clear()
        self.driver.find_element(By.ID,self.username_field_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def get_welcome_text(self):
        welcome_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.welcome_text_id))
        )
        print(welcome_element.get_attribute('outerHTML'))
        return welcome_element.text


    def click_logout_optn(self):
        self.driver.find_element(By.ID, self.logout_option_id).click()

