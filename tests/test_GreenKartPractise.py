import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import BaseClass
from pageObject.Common_Elements import Common_Elements
from pageObject.GK_HomePage import GK_HomePage
from pageObject.GK_OfferPage import GK_OfferPage


class Test_GreenKartPractise(BaseClass):

    def test_searchAndaddtoCart_functionality(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        gk_hompage = GK_HomePage(self.driver)
        ProductPrice = []
        gk_hompage.getSearchBox().send_keys("Apple")
        ProductPrice.append(gk_hompage.getDynProductPrice("Apple").text)
        gk_hompage.getDynAddToCartBtn("Apple").click()
        gk_hompage.getSearchBox().clear()
        gk_hompage.getSearchBox().send_keys("Banana")
        ProductPrice.append(gk_hompage.getDynProductPrice("Banana").text)
        gk_hompage.getDynAddToCartBtn("Banana").click()
        itemcount = gk_hompage.getItemCount().text
        assert int(itemcount) == int(2)
        ActPrice = gk_hompage.getPrice().text
        Total = 0
        for price in ProductPrice:
            Total += int(price)
        assert int(ActPrice) == int(Total)


    def test_searchAndQuantity_functionality(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        gk_hompage = GK_HomePage(self.driver)
        common_elements = Common_Elements(self.driver)
        wait = WebDriverWait(self.driver, 5)
        PriceOf1QuantityList = gk_hompage.getDynProductPrice("Mango").text
        gk_hompage.getDynQuantityBtn("Mango").clear()
        gk_hompage.getDynQuantityBtn("Mango").send_keys(5) #75*5= 375
        gk_hompage.getDynAddToCartBtn("Mango").click()
        #verify the Decrease button functionality
        wait.until(expected_conditions.invisibility_of_element_located(common_elements.findButtonByText("ADDED")))
        gk_hompage.getDynDecrementBtn("Mango").click()  # 75*4 = 300
        gk_hompage.getDynAddToCartBtn("Mango").click()
        wait.until(expected_conditions.invisibility_of_element_located(common_elements.findButtonByText("ADDED")))
        gk_hompage.getDynIncrementBtn("Mango").click()  # 75*5= 375
        gk_hompage.getDynAddToCartBtn("Mango").click()
        gk_hompage.getCartIcon().click()
        ActQunatity = gk_hompage.getDynProductQuantity_cartPreview("Mango").text
        ActPrice = gk_hompage.getDynProductPrice_cartPreview("Mango").text
        assert "14" in ActQunatity
        assert int(ActPrice) == int(PriceOf1QuantityList)*int(14)

    def test_AddToCartAndRemoveOnPreview_functionality(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        gk_hompage = GK_HomePage(self.driver)
        common_elements = Common_Elements(self.driver)
        gk_hompage.getDynAddToCartBtn("Cucumber").click()
        gk_hompage.getDynAddToCartBtn("Pumpkin").click()
        gk_hompage.getDynAddToCartBtn("Raspberry").click()
        gk_hompage.getDynAddToCartBtn("Cashews").click()
        gk_hompage.getCartIcon().click()
        #verify that element is displayed and remove it
        self.elementShouldBeVisible(gk_hompage.getDynProductName_cartPreview("Cucumber"))
        gk_hompage.getDynRemoveBtn_CartPreview("Cucumber").click()
        self.elementShouldBeVisible(gk_hompage.getDynProductName_cartPreview("Pumpkin"))
        gk_hompage.getDynRemoveBtn_CartPreview("Pumpkin").click()
        self.elementShouldBeVisible(gk_hompage.getDynProductName_cartPreview("Raspberry"))
        gk_hompage.getDynRemoveBtn_CartPreview("Raspberry").click()
        self.elementShouldBeVisible(gk_hompage.getDynProductName_cartPreview("Cashews"))
        gk_hompage.getDynRemoveBtn_CartPreview("Cashews").click()
        common_elements.getFindElementByText("You cart is empty!")

    def test_TopDeals_WebTableSorting_Functionality(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        gk_hompage = GK_HomePage(self.driver)
        gk_offerpage = GK_OfferPage(self.driver)
        common_elements = Common_Elements(self.driver)
        gk_hompage.getTopDealsLinkText().click()
        windowhandles = self.driver.window_handles
        self.driver.switch_to.window(windowhandles[1])
        wait = WebDriverWait(self.driver, 5)
        Deliverydatefield = common_elements.findElementByText("Delivery Date")
        wait.until(expected_conditions.visibility_of_element_located(Deliverydatefield))
        self.selectByValue(gk_offerpage.getPageSize(), '20')
        ActVegFruitNameList = []
        ExpectedActVegFruitNameList = []
        products = gk_offerpage.getCommonVegFruitRow()
        for product in products:
            ActVegFruitNameList.append(product.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text)
        print(ActVegFruitNameList)
        print(sorted(ActVegFruitNameList))
        ExpectedActVegFruitNameList = sorted(ActVegFruitNameList)
        gk_offerpage.getVegFruitNameColHeader().click()
        ActSortVegFruitNameList = []
        sortProducts = gk_offerpage.getCommonVegFruitRow()
        for sortproduct in sortProducts:
            ActSortVegFruitNameList.append(sortproduct.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text)
        assert ExpectedActVegFruitNameList == ActSortVegFruitNameList
        print("Verification completed! Sorting functionality is working as expected")

    def test_TopDeals_DeliveryDate_field_functionality(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        gk_hompage = GK_HomePage(self.driver)
        gk_offerpage = GK_OfferPage(self.driver)
        common_elements = Common_Elements(self.driver)
        gk_hompage.getTopDealsLinkText().click()
        windowhandles = self.driver.window_handles
        self.driver.switch_to.window(windowhandles[1])
        wait = WebDriverWait(self.driver, 5)
        self.elementShouldBeVisible(common_elements.getFindElementByText("Delivery Date"))
        initialValue = gk_offerpage.getDeliveryDateInput().get_dom_attribute("value")
        print(initialValue)
        todaysDate = self.get_todays_date("%Y-%m-%d")
        print(todaysDate)
        assert todaysDate == initialValue
        gk_offerpage.getDeliveryDateClearBtn().click()
        time.sleep(2)
        inputDate = self.getFutureDate(10, "%Y-%m-%d")
        print(inputDate)
        inputDateList = inputDate.split('-')
        print(inputDateList)
        gk_offerpage.getMonthInput().send_keys(inputDateList[1])
        gk_offerpage.getDayInput().send_keys(inputDateList[2])
        gk_offerpage.getYearInput().send_keys(inputDateList[0])
        currentValue = gk_offerpage.getDeliveryDateInput().get_dom_attribute("value")
        print(currentValue)
        assert not initialValue == currentValue