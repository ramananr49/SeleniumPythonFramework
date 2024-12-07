from selenium.webdriver.common.by import By


class SP_MainPage:

    def __init__(self, driver):
        self.driver = driver

    radioBtnTitle = (By.XPATH, "//div[@id='radio-btn-example']//legend")
    radio1Btn = (By.XPATH, "//input[@value='radio1']")
    radio2Btn = (By.XPATH, "//input[@value='radio2']")
    radio3Btn = (By.XPATH, "//input[@value='radio3']")

    checkBoxTitle = (By.XPATH, "//div[@id='checkbox-example']//legend")
    checkBoxes = (By.XPATH, "//div[@id='checkbox-example']//input[@type='checkbox']")
    option1CheckBox = (By.XPATH, "//input[@id='checkBoxOption1']")
    option2CheckBox = (By.XPATH, "//input[@id='checkBoxOption2']")
    option3CheckBox = (By.XPATH, "//input[@id='checkBoxOption3']")

    dropDownTitle = (By.CSS_SELECTOR, ".cen-right-align legend")
    stDropDown = (By.ID, "dropdown-class-example")

    dynamicDropdownTitle = (By.XPATH, "//div[@id='select-class-example']//legend")
    dynDropdownTextBox = (By.CSS_SELECTOR, "input#autocomplete")


    def getRadioBrnTitle(self):
        return self.driver.find_element(*SP_MainPage.radioBtnTitle)

    def getRadio1Btn(self):
        return self.driver.find_element(*SP_MainPage.radio1Btn)

    def getRadio2Btn(self):
        return self.driver.find_element(*SP_MainPage.radio2Btn)

    def getRadio3Btn(self):
        return self.driver.find_element(*SP_MainPage.radio3Btn)

    def getCheckBoxTitle(self):
        return self.driver.find_element(*SP_MainPage.checkBoxTitle)

    def getCheckBoxes(self):
        return self.driver.find_elements(*SP_MainPage.checkBoxes)

    def getDropDownTitle(self):
        return self.driver.find_element(*SP_MainPage.dropDownTitle)

    def getDropDown(self):
        return self.driver.find_element(*SP_MainPage.stDropDown)

    def getDynamicDropdownTitle(self):
        return self.driver.find_element(*SP_MainPage.dynamicDropdownTitle)

    def getdynDropdownTextBox(self):
        return self.driver.find_element(*SP_MainPage.dynDropdownTextBox)

    def dynamicDropdownOption(self, country):
        return (By.XPATH, f"//div[@class = 'ui-menu-item-wrapper' and text()='{country}']")

    def getDynamicDropdownOption(self, Country):
        countryname = self.dynamicDropdownOption(Country)
        return self.driver.find_element(*countryname)