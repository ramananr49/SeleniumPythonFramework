from selenium.webdriver.common.by import By


class PC_ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver

    countryTxtBox = (By.ID, "country")
    iAgreeCheckbox = (By.ID, "checkbox2")
    purchaseBtn = (By.CSS_SELECTOR, "input[value='Purchase']")
    successToastMsg = (By.CSS_SELECTOR, "div[class*='alert-success']")
    dismissBtn = (By.CSS_SELECTOR, "a[class='close']")

    def getCountryTextBox(self):
        return self.driver.find_element(*PC_ConfirmationPage.countryTxtBox)

    def getIAgreeCheckBox(self):
        return self.driver.find_element(*PC_ConfirmationPage.iAgreeCheckbox)

    def getPurchaseButton(self):
        return self.driver.find_element(*PC_ConfirmationPage.purchaseBtn)

    def getSuccessToastMessage(self):
        return self.driver.find_element(*PC_ConfirmationPage.successToastMsg)

    def getDismissButton(self):
        return self.driver.find_element(*PC_ConfirmationPage.dismissBtn)