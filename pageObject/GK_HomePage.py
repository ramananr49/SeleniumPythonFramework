from selenium.webdriver.common.by import By


class GK_HomePage:
    def __init__(self, driver):
        self.driver = driver

    searchBox = (By.CSS_SELECTOR, 'input.search-keyword')
    productNames = (By.XPATH, "//div[@class='product']/h4")
    AddToCartBtns = (By.XPATH, "//div[@class='product-action']/button")
    cartIcon = (By.XPATH, "//img[@alt='Cart']")
    proceedToCheckOutBtn = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    TopDeals = (By.LINK_TEXT, "Top Deals")
    itemsCount = (By.XPATH, "//td[text()='Items']/following-sibling::td[2]")
    Price = (By.XPATH, "//td[text()='Price']/following-sibling::td[2]")

    def getSearchBox(self):
        return self.driver.find_element(*GK_HomePage.searchBox)

    def getProductNames(self):
        return self.driver.find_elements(*GK_HomePage.productNames)

    def getAddToCartBtns(self):
        return self.driver.find_elements(*GK_HomePage.AddToCartBtns)

    def getCartIcon(self):
        return self.driver.find_element(*GK_HomePage.cartIcon)

    def getProceedToCheckOutBtn(self):
        return self.driver.find_element(*GK_HomePage.proceedToCheckOutBtn)

    def getTopDealsLinkText(self):
        return self.driver.find_element(*GK_HomePage.TopDeals)

    def getItemCount(self):
        return self.driver.find_element(*GK_HomePage.itemsCount)

    def getPrice(self):
        return self.driver.find_element(*GK_HomePage.Price)

    ####################################Below are Dynamic webelement locator####################################

    def dynamicIncrementBtn(self, vegetable_name):
        return (By.XPATH, f"//h4[contains(text(),'{vegetable_name}')]/following-sibling::div/a[@class='increment']")

    def getDynIncrementBtn(self, veg_name):
        incrementBtn = self.dynamicIncrementBtn(veg_name)
        return self.driver.find_element(*incrementBtn)

    def dynamicDecrementBtn(self, vegetable_name):
        return (By.XPATH, f"//h4[contains(text(),'{vegetable_name}')]/following-sibling::div/a[@class='decrement']")

    def getDynDecrementBtn(self, veg_name):
        decrementBtn = self.dynamicDecrementBtn(veg_name)
        return self.driver.find_element(*decrementBtn)

    def dynamicQuantityBtn(self, vegetable_name):
        return (By.XPATH, f"//h4[contains(text(),'{vegetable_name}')]/following-sibling::div/input[@class='quantity']")

    def getDynQuantityBtn(self, veg_name):
        quantityBtn = self.dynamicQuantityBtn(veg_name)
        return self.driver.find_element(*quantityBtn)

    def dynamicAddToCartBtn(self, vegetable_name):
        return (By.XPATH, f"//h4[contains(text(), '{vegetable_name}')]/following-sibling::div[@class='product-action']/button")

    def getDynAddToCartBtn(self, veg_name):
        addToCartBtn = self.dynamicAddToCartBtn(veg_name)
        return self.driver.find_element(*addToCartBtn)

    def dynamicProductPrice(self, vegetable_name):
        return (By.XPATH, f"//h4[contains(text(), '{vegetable_name}')]/following-sibling::p")

    def getDynProductPrice(self, veg_name):
        productprice = self.dynamicProductPrice(veg_name)
        return self.driver.find_element(*productprice)

    def dynamicProductQuantity_cartPreview(self, vegetable_name):
        return (By.XPATH, f"(//p[contains(text(), '{vegetable_name}')]/parent::div/following-sibling::div/p[@class='quantity'])[1]")

    def getDynProductQuantity_cartPreview(self, veg_name):
        productQuantity_cartPreview = self.dynamicProductQuantity_cartPreview(veg_name)
        return self.driver.find_element(*productQuantity_cartPreview)

    def dynamicProductPrice_cartPreview(self, vegetable_name):
        return (By.XPATH, f"(//p[contains(text(), '{vegetable_name}')]/parent::div/following-sibling::div/p[@class='amount'])[1]")

    def getDynProductPrice_cartPreview(self, veg_name):
        productPrice_cartPreview = self.dynamicProductPrice_cartPreview(veg_name)
        return self.driver.find_element(*productPrice_cartPreview)

    def dynamicRemoveBtn_CartPreview(self, vegetable_name):
        return (By.XPATH, f"(//p[contains(text(), '{vegetable_name}')]/parent::div/following-sibling::a)[1]")

    def getDynRemoveBtn_CartPreview(self, veg_name):
        removeIcon = self.dynamicRemoveBtn_CartPreview(veg_name)
        return self.driver.find_element(*removeIcon)

    def dynamicProductName_CartPreview(self, vegetable_name):
        return (By.XPATH, f"(//p[contains(text(), '{vegetable_name}')])[1]")

    def getDynProductName_cartPreview(self, veg_name):
        product_name = self.dynamicProductName_CartPreview(veg_name)
        return self.driver.find_element(*product_name)