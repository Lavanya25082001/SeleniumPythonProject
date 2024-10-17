
import time
from base_pages.Categories_Page import CategoriesPage
from utilities.read_properties import Read_Config
from utilities.loggers import  log_maker
from selenium.webdriver.common.by import By

class TestCategories:
    blazedemo_URL = Read_Config.get_admin_page_url()
    logger = log_maker.log_gen()
    def test_category_mobile(self, setup):
        self.logger.info("Verification of mobile category")
        driver = setup
        driver.get(self.blazedemo_URL)
        time.sleep(3)
        category_module=CategoriesPage(driver)
        self.logger.info("Selecting random product from mobile category")
        category_module.selecting_mobile()
        self.logger.info("add to cart")
        time.sleep(3)
        category_module.addToCart()
        time.sleep(3)
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        self.logger.info("Handling Message alert")
        time.sleep(3)
        category_module.place_order()
        time.sleep(3)
        category_module.fill_form_with_fake_data()
        self.logger.info("User placed order successfully")

    def test_category_laptop(self,setup):
        self.logger.info("Verification of laptop category")
        driver = setup
        driver.get(self.blazedemo_URL)
        time.sleep(3)
        category_module = CategoriesPage(driver)
        self.logger.info("Selecting random product from laptop category")
        category_module.selecting_laptops_optn()
        self.logger.info("add to cart")
        time.sleep(3)
        category_module.addToCart()
        time.sleep(3)
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        self.logger.info("Handling Message alert")
        time.sleep(3)
        category_module.place_order()
        time.sleep(3)
        category_module.fill_form_with_fake_data()
        self.logger.info("User placed order for laptop successfully")

    def test_category_monitor(self, setup):
        self.logger.info("Verification of monitor category")
        driver = setup
        driver.get(self.blazedemo_URL)
        time.sleep(3)
        category_module = CategoriesPage(driver)
        self.logger.info("Selecting random product from laptop category")
        category_module.selecting_monitors_optn()
        self.logger.info("add to cart")
        time.sleep(3)
        category_module.addToCart()
        time.sleep(3)
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        self.logger.info("Handling Message alert")
        time.sleep(3)
        category_module.place_order()
        time.sleep(3)
        category_module.fill_form_with_fake_data()
        self.logger.info("User placed order for laptop successfully")


