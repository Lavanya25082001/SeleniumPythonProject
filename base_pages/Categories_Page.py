import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
fake = Faker()

class CategoriesPage:
    categories_xpath='//a[@id="cat"]'
    phones_optn_xpath='//a[text()="Phones"]'
    laptops_optn_xpath='//a[text()="Laptops"]'
    monitors_optn_xpath='//a[text()="Monitors"]'
    product_elements_xpath ='//h4[@class="card-title"]/a'
    addToCart_button_xpath='//a[contains(@class,"btn-success")]'
    cart_optn_xpath='//a[@id="cartur"]'
    place_order_btn_xpath='//button[normalize-space()="Place Order"]'
    name_field_id="(//div[@class='modal-content']//div[@class='modal-body']//form)[3]//div[@class='form-group']/label[@for='name']//../input"
    country_field_id='country'
    city_field_id='city'
    creditcard_field_id='card'
    month_field_id='month'
    year_field_id='year'
    purchase_btn_xpath='//button[normalize-space()="Purchase"]'
    confirmation_text_xpath='//h2[normalize-space()="Thank you for your purchase!"]'
    ok_btn_xpath='//button[text()="OK"]'



    def __init__(self,driver):
        self.driver=driver


    def selecting_mobile(self):
        self.driver.find_element(By.XPATH, self.categories_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.phones_optn_xpath).click()
        product_elements = self.driver.find_elements(By.XPATH, self.product_elements_xpath)
        self.product_count = len(product_elements)
        print(f'Total Product Count: {self.product_count}')
        if self.product_count > 0:
            random_product_index = random.randint(0, self.product_count - 1)
            product_elements[random_product_index].click()
        else:
            print("No products available to select.")

    def addToCart(self):
        self.driver.find_element(By.XPATH,self.addToCart_button_xpath).click()

    def place_order(self):
        self.driver.find_element(By.XPATH, self.cart_optn_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.place_order_btn_xpath).click()

    def fill_form_with_fake_data(self):
        fake_name = fake.name()
        fake_country = fake.country()
        fake_city = fake.city()
        fake_credit_card = fake.credit_card_number()
        fake_month = fake.month()
        fake_year = fake.year()
        # Fill the form with fake data
        self.driver.find_element(By.XPATH, self.name_field_id).click()
        self.driver.find_element(By.XPATH, self.name_field_id).send_keys(fake_name)
        self.driver.find_element(By.ID, self.country_field_id).send_keys(fake_country)
        self.driver.find_element(By.ID, self.city_field_id).send_keys(fake_city)
        self.driver.find_element(By.ID, self.creditcard_field_id).send_keys(fake_credit_card)
        self.driver.find_element(By.ID, self.month_field_id).send_keys(fake_month)
        self.driver.find_element(By.ID, self.year_field_id).send_keys(fake_year)
        self.driver.find_element(By.XPATH, self.purchase_btn_xpath).click()
        confirmation_text=self.driver.find_element(By.XPATH,self.confirmation_text_xpath).text
        expected_confirmation_text='Thank you for your purchase!'
        assert confirmation_text==expected_confirmation_text
        self.driver.find_element(By.XPATH, self.ok_btn_xpath).click()
        time.sleep(3)

    def selecting_laptops_optn(self):
        self.driver.find_element(By.XPATH, self.laptops_optn_xpath).click()
        time.sleep(10)
        product_elements = self.driver.find_elements(By.XPATH, self.product_elements_xpath)
        self.product_count = len(product_elements)
        print(f'Total Product Count: {self.product_count}')
        if self.product_count > 0:
            random_product_index = random.randint(0, self.product_count - 1)
            product_elements[random_product_index].click()
        else:
            print("No products available to select.")



    def selecting_monitors_optn(self):
        self.driver.find_element(By.XPATH, self.monitors_optn_xpath).click()
        time.sleep(10)
        product_elements = self.driver.find_elements(By.XPATH, self.product_elements_xpath)
        self.product_count = len(product_elements)
        print(f'Total Product Count: {self.product_count}')
        if self.product_count > 0:
            random_product_index = random.randint(0, self.product_count - 1)
            product_elements[random_product_index].click()
        else:
            print("No products available to select.")


