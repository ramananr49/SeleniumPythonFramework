import time

from selenium import webdriver

from Utilities.BaseClass import BaseClass
from pageObject.GK_HomePage import GK_HomePage


class Test_GK_DynamicXpathCheck(BaseClass):

    def test_dynamicXpathCheck(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

        gk_homepage = GK_HomePage(self.driver)
        gk_homepage.getDynQuantityBtn("Apple").send_keys(10)
        time.sleep(4)
        gk_homepage.getDynDecrementBtn("Apple").click()
        time.sleep(4)
        gk_homepage.getDynIncrementBtn("Apple").click()
        time.sleep(4)
        DRIVER = webdriver.Chrome()