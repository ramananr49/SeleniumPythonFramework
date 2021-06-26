from selenium.webdriver.common.by import By


class GK_HomePage:
    def __init__(self, driver):
        self.driver = driver

    searchBox = (By.CSS_SELECTOR, 'input.search-keyword')

    def getSearchBox(self):
        return self.driver.find_element(*GK_HomePage.searchBox)

    productNames = (By.XPATH, "//div[@class='product']/h4")

    def getProductNames(self):
        return self.driver.find_elements(*GK_HomePage.productNames)

    AddToCartBtns = (By.XPATH, "//div[@class='product-action']/button")

    def getAddToCartBtns(self):
        return self.driver.find_elements(*GK_HomePage.AddToCartBtns)

    cartIcon = (By.XPATH, "//img[@alt='Cart']")

    def getCartIcon(self):
        return self.driver.find_element(*GK_HomePage.cartIcon)

    proceedToCheckOutBtn = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def getProceedToCheckOutBtn(self):
        return self.driver.find_element(*GK_HomePage.proceedToCheckOutBtn)



