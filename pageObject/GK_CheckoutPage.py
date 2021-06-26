from selenium.webdriver.common.by import By


class GK_CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    productNamesInTable = (By.CSS_SELECTOR, "p.product-name")

    def getProductNamesInTable(self):
        return self.driver.find_elements(*GK_CheckoutPage.productNamesInTable)

    totalAfterDiscount = (By.CLASS_NAME, "discountAmt")

    def getTotalAfterDiscount(self):
        return self.driver.find_element(*GK_CheckoutPage.totalAfterDiscount)

