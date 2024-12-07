from selenium.webdriver.common.by import By


class PC_ShopPage:

    def __init__(self, driver):
        self.driver = driver

    ProtoCommerceHome = (By.XPATH, "//a[text()='ProtoCommerce Home']")
    Checkout_btn = (By.XPATH, "//a[contains(text(), 'Checkout')]")

    def getProtoCommerceHome(self):
        return self.driver.find_element(*PC_ShopPage.ProtoCommerceHome)

    def getChecoutBtn(self):
        return self.driver.find_element(*PC_ShopPage.Checkout_btn)

    def dynamicProductHeader(self, product_name):
        return (By.XPATH, f"//h4[@class='card-title']/a[text()='{product_name}']")

    def getDynProductHeader(self, productName):
        product_Name = self.dynamicProductHeader(productName)
        return self.driver.find_element(*product_Name)

    def dynamicProductPrice(self, product_name):
        return (By.XPATH, f"//a[text()='{product_name}']/parent::h4/following-sibling::h5")

    def getDynProductPrice(self, productName):
        productprice = self.dynamicProductPrice(productName)
        return self.driver.find_element(*productprice)

    def dynamicAddBtn(self, product_name):
        return (By.XPATH, f"//a[text()='{product_name}']/ancestor::div[@class='card-body']/following-sibling::div/button")

    def getDynAddBtn(self, productName):
        addBtn = self.dynamicAddBtn(productName)
        return self.driver.find_element(*addBtn)