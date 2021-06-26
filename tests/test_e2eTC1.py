import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import BaseClass
from pageObject.GK_CheckoutPage import GK_CheckoutPage
from pageObject.GK_HomePage import GK_HomePage


class Test_prospectModule(BaseClass):

    def test_GreenCardFnValidation(self):

        # variables
        ActNames = []
        ExpNames = ["Cucumber", "Raspberry", "Strawberry"]
        ActProducts = []
        expProducts = []
        summation = 0
        wait = WebDriverWait(self.driver, 8)
        self.driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
        homePage = GK_HomePage(self.driver)

        print('Check 01:- Verify that Search functionality in home page is working fine')
        #self.driver.find_element_by_css_selector('input.search-keyword').send_keys("ber")
        homePage.getSearchBox().send_keys("ber")
        #Names = self.driver.find_elements_by_xpath("//div[@class='product']/h4")
        Names = homePage.getProductNames()

        for Name in Names:
            ActNames.append(Name.text.split("-")[0].strip())

        print(ActNames)
        print(ExpNames)
        assert ActNames == ExpNames
        print('Check 01:- Verification completed')

        time.sleep(1)
        print("Check 02:- Verify whether Product selected in page 1 are showing in Checkout page")
        #buttons = self.driver.find_elements_by_xpath("//div[@class='product-action']/button")
        buttons = homePage.getAddToCartBtns()
        for button in buttons:
            button.click()
            print(button.find_element_by_xpath("parent::div//parent::div/h4").text.split("-")[
                      0].strip() + " added to the Cart")
            ActProducts.append(button.find_element_by_xpath("parent::div//parent::div/h4").text)

        #self.driver.find_element_by_xpath("//img[@alt='Cart']").click()
        homePage.getCartIcon().click()
        #self.driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
        homePage.getProceedToCheckOutBtn().click()
        time.sleep(1)
        checkoutPage = GK_CheckoutPage(self.driver)
        #veggies = self.driver.find_elements_by_css_selector("p.product-name")
        veggies = checkoutPage.getProductNamesInTable()
        for veg in veggies:
            expProducts.append(veg.text)

        print(ActProducts)
        print(expProducts)
        assert ActProducts == expProducts
        print('Check 02:- Verification completed')

        print("Check 03:- Verify Total Price is decreases after applied the discount")

        #beforeTotal = int(self.driver.find_element_by_class_name("discountAmt").text)
        beforeTotal = int(checkoutPage.getTotalAfterDiscount().text)
        self.driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
        self.driver.find_element_by_class_name("promoBtn").click()
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
        ActText = self.driver.find_element_by_class_name("promoInfo").text
        ExpText = "Code applied ..!"
        #afterTotal = float(self.driver.find_element_by_class_name("discountAmt").text)
        afterTotal = float(checkoutPage.getTotalAfterDiscount().text)

        assert afterTotal < beforeTotal
        assert ActText == ExpText
        print(beforeTotal)
        print(afterTotal)
        print(ActText)
        print('Check 03:- Verification completed')

        print("Check 04:- Verify if sum of products in checkout page matches with Total Amount")

        amounts = self.driver.find_elements_by_xpath("//tr/td[5]/p[@class='amount']")

        for amount in amounts:
            summation = summation + int(amount.text)

        print(summation)
        Total = int(self.driver.find_element_by_class_name("totAmt").text)

        print("{}{}".format("Total is ", Total))
        assert Total == summation
        print('Check 04:- Verification completed')
