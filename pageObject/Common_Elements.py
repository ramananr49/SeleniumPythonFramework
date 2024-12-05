from selenium.webdriver.common.by import By


class Common_Elements:

    def __init__(self, driver):
        self.driver = driver

    def findButtonByText(self, button_name):
        return (By.XPATH, f"//button[contains(text(),'{button_name}')]")

    def getFindButtonByText(self, btn_name):
        findBtnName = self.findButtonByText(btn_name)
        return self.driver.find_element(*findBtnName)

    def findElementByText(self, element_name):
        return (By.XPATH, f"//*[contains(text(),'{element_name}')]")

    def getFindElementByText(self, ele_name):
        findEleName = self.findElementByText(ele_name)
        return self.driver.find_element(*findEleName)