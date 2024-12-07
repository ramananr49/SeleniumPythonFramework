from selenium.webdriver.common.by import By


class PC_CartPage:

    def __init__(self, driver):
        self.driver = driver

    totalAmountText = (By.CSS_SELECTOR, "td[class='text-right'] h3")
    continueShoppingBtn = (By.CSS_SELECTOR, "button[class*='btn-default']")
    checkoutBtn = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def getTotalAmountText(self):
        return not self.driver.find_element(*PC_CartPage.totalAmountText)

    def getContinueShoppingButton(self):
        return self.driver.find_element(*PC_CartPage.continueShoppingBtn)

    def getCheckoutButton(self):
        return self.driver.find_element(*PC_CartPage.checkoutBtn)

    def dynamicQuantityTextbox(self, product_name):
        return (By.XPATH, f"//a[text()='{product_name}']/ancestor::td/following-sibling::td/input[@id='exampleInputEmail1']")

    def getDynQuantityTextBox(self, productname):
        quantity = self.dynamicQuantityTextbox(productname)
        return self.driver.find_element(*quantity)

    def dynamic1unitPrice(self, productname):
        return (By.XPATH, f"//a[text()='{productname}']/ancestor::td/following-sibling::td[2]")

    def getDyn1UnitPrice(self, product_name):
        price = self.dynamic1unitPrice(product_name)
        return self.driver.find_element(*price)

    def dynamicTotal(self, productname):
        return (By.XPATH, f"//a[text()='{productname}']/ancestor::td/following-sibling::td[3]")

    def getDynTotal(self, product_name):
        total = self.dynamicTotal(product_name)
        return self.driver.find_element(*total)

    def dynamicRemovebtn(self, productname):
        return (By.XPATH, f"//a[text()='{productname}']/ancestor::td/following-sibling::td/button")

    def getDynRemoveButton(self, product_name):
        removebtn =self.dynamicRemovebtn(product_name)
        return self.driver.find_element(*removebtn)