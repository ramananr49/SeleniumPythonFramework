import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass
from pageObject.Common_Elements import Common_Elements
from pageObject.PC_CartPage import PC_CartPage
from pageObject.PC_ConfirmationPage import PC_ConfirmationPage
from pageObject.PC_HomePage import PC_HomePage
from pageObject.PC_ShopPage import PC_ShopPage


class Test_ProtoCommercePractise(BaseClass):

    def test_verifyThatAddingSameProductMultipleTime(self):

        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        pc_homepage = PC_HomePage(self.driver)
        pc_shoppage = PC_ShopPage(self.driver)
        pc_cartpage = PC_CartPage(self.driver)
        pc_homepage.getShopTab().click()
        pc_shoppage.getDynAddBtn("iphone X").click()
        pc_shoppage.getDynAddBtn("iphone X").click()
        pc_shoppage.getChecoutBtn().click()
        ActQuantity = pc_cartpage.getDynQuantityTextBox("iphone X").get_attribute('value')
        assert int(ActQuantity) == 2
        singleUnitPrice = pc_cartpage.getDyn1UnitPrice("iphone X").text
        ActsingleUnitPrice = singleUnitPrice.split(" ")
        ComputingTotal = int(ActsingleUnitPrice[1]) * int(ActQuantity)
        ActTotal = pc_cartpage.getDynTotal("iphone X").text
        assert str(ComputingTotal) in ActTotal

    def test_AddAllTheProduct(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        pc_homepage = PC_HomePage(self.driver)
        pc_shoppage = PC_ShopPage(self.driver)
        pc_cartpage = PC_CartPage(self.driver)
        pc_homepage.getShopTab().click()
        pc_shoppage.getDynAddBtn("iphone X").click()
        pc_shoppage.getDynAddBtn("Samsung Note 8").click()
        pc_shoppage.getDynAddBtn("Nokia Edge").click()
        pc_shoppage.getDynAddBtn("Blackberry").click()
        pc_shoppage.getChecoutBtn().click()
        assert 1 == int(pc_cartpage.getDynQuantityTextBox("iphone X").get_attribute('value'))
        assert 1 == int(pc_cartpage.getDynQuantityTextBox("Samsung Note 8").get_attribute('value'))
        assert 1 == int(pc_cartpage.getDynQuantityTextBox("Nokia Edge").get_attribute('value'))
        assert 1 == int(pc_cartpage.getDynQuantityTextBox("Blackberry").get_attribute('value'))
        iphoneTotal = pc_cartpage.getDynTotal("iphone X").text.split(" ")
        SamsungTotal = pc_cartpage.getDynTotal("Samsung Note 8").text.split(" ")
        NokiaTotal = pc_cartpage.getDynTotal("Nokia Edge").text.split(" ")
        BlackberryTotal = pc_cartpage.getDynTotal("Blackberry").text.split(" ")
        productTotal = int(iphoneTotal[1]) + int(SamsungTotal[1]) + int(NokiaTotal[1]) + int(BlackberryTotal[1])
        print(productTotal)
        script = "return document.querySelector('td[class=\"text-right\"] h3').innerText;"
        print(script)
        ActTotalAmount = self.driver.execute_script(script)
        assert str(productTotal) in ActTotalAmount

    def test_verifyTheContinueShippingAndRemove_functionality(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        pc_homepage = PC_HomePage(self.driver)
        pc_shoppage = PC_ShopPage(self.driver)
        pc_cartpage = PC_CartPage(self.driver)
        pc_homepage.getShopTab().click()
        pc_shoppage.getDynAddBtn("iphone X").click()
        pc_shoppage.getDynAddBtn("Samsung Note 8").click()
        pc_shoppage.getChecoutBtn().click()
        assert 1 == int(pc_cartpage.getDynQuantityTextBox("iphone X").get_attribute('value'))
        assert 1 == int(pc_cartpage.getDynQuantityTextBox("Samsung Note 8").get_attribute('value'))
        pc_cartpage.getContinueShoppingButton().click()
        pc_shoppage.getDynAddBtn("iphone X").click()
        pc_shoppage.getDynAddBtn("Samsung Note 8").click()
        pc_shoppage.getDynAddBtn("Nokia Edge").click()
        pc_shoppage.getDynAddBtn("Blackberry").click()
        pc_shoppage.getChecoutBtn().click()
        assert 1 == int(pc_cartpage.getDynQuantityTextBox("iphone X").get_attribute('value'))
        assert 1 == int(pc_cartpage.getDynQuantityTextBox("Samsung Note 8").get_attribute('value'))
        assert 1 == int(pc_cartpage.getDynQuantityTextBox("Nokia Edge").get_attribute('value'))
        assert 1 == int(pc_cartpage.getDynQuantityTextBox("Blackberry").get_attribute('value'))
        pc_cartpage.getDynRemoveButton("iphone X").click()
        pc_cartpage.getDynRemoveButton("Samsung Note 8").click()
        pc_cartpage.getDynRemoveButton("Nokia Edge").click()
        pc_cartpage.getDynRemoveButton("Blackberry").click()
        script = "return document.querySelector('td[class=\"text-right\"] h3').innerText;"
        print(script)
        assert "0" in self.driver.execute_script(script)

    def test_verifyIncreamentOfQuantityInCartPage(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        pc_homepage = PC_HomePage(self.driver)
        pc_shoppage = PC_ShopPage(self.driver)
        pc_cartpage = PC_CartPage(self.driver)
        pc_homepage.getShopTab().click()
        pc_shoppage.getDynAddBtn("Nokia Edge").click()
        pc_shoppage.getDynAddBtn("Blackberry").click()
        pc_shoppage.getChecoutBtn().click()
        assert 1 == int(pc_cartpage.getDynQuantityTextBox("Nokia Edge").get_attribute('value'))
        assert 1 == int(pc_cartpage.getDynQuantityTextBox("Blackberry").get_attribute('value'))
        pc_cartpage.getDynQuantityTextBox("Nokia Edge").clear()
        pc_cartpage.getDynQuantityTextBox("Nokia Edge").send_keys(2)
        NokiaTotal = pc_cartpage.getDynTotal("Nokia Edge").text.split(" ")
        pc_cartpage.getDynQuantityTextBox("Blackberry").clear()
        pc_cartpage.getDynQuantityTextBox("Blackberry").send_keys(2)
        BlackberryTotal = pc_cartpage.getDynTotal("Blackberry").text.split(" ")
        grandTotal = int(NokiaTotal[1]) + int(BlackberryTotal[1])
        script = "return document.querySelector('td[class=\"text-right\"] h3').innerText"
        print(script)
        assert str(grandTotal) in (self.driver.execute_script(script))

    def test_verifyTheEndToEnd_functionality(self):
        log = self.getLogger()
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        pc_homepage = PC_HomePage(self.driver)
        pc_shoppage = PC_ShopPage(self.driver)
        pc_cartpage = PC_CartPage(self.driver)
        pc_confirmPage = PC_ConfirmationPage(self.driver)
        commonElements = Common_Elements(self.driver)
        pc_homepage.getShopTab().click()
        pc_shoppage.getDynAddBtn("Nokia Edge").click()
        pc_shoppage.getDynAddBtn("Samsung Note 8").click()
        pc_shoppage.getChecoutBtn().click()
        log.info("Verify the added product Quantity")
        assert 1 == int(pc_cartpage.getDynQuantityTextBox("Nokia Edge").get_attribute('value'))
        assert 1 == int(pc_cartpage.getDynQuantityTextBox("Samsung Note 8").get_attribute('value'))
        pc_cartpage.getCheckoutButton().click()
        pc_confirmPage.getCountryTextBox().send_keys("India")
        wait.until(expected_conditions.visibility_of_element_located(commonElements.findElementByText("India")))
        commonElements.getFindElementByText("India").click()
        wait.until(expected_conditions.invisibility_of_element_located(pc_confirmPage.dropdownPopup))
        pc_confirmPage.getIAgreeCheckBox().click()
        pc_confirmPage.getPurchaseButton().click()
        toastmsg = pc_confirmPage.getSuccessToastMessage().text
        # self.elementShouldBeVisible(toastmsg)
        self.elementShouldBePresent(pc_confirmPage.successToastMsg)
        assert "Success!" in toastmsg
        pc_confirmPage.getDismissButton().click()
        # self.elementShouldNotBeVisible(toastmsg)
        self.elementShouldNotBePresent(pc_confirmPage.successToastMsg)
        log.info("Verification Completed")