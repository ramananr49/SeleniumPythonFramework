from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass
from pageObject.Common_Elements import Common_Elements
from pageObject.SP_MainPage import SP_MainPage


class Test_SeleniumPacticePage(BaseClass):

    def test_RadioBtn_Handling(self):
        #variable
        ExpRadioTitle = "Radio Button Example"

        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        SPracticePage = SP_MainPage(self.driver)
        ActText = SPracticePage.getRadioBrnTitle().text
        assert ActText == ExpRadioTitle
        SPracticePage.getRadio2Btn().click()
        ActVal = SPracticePage.getRadio2Btn().is_selected()
        assert ActVal

    def test_CheckBox_Handling(self):
        #variable
        ExpCBText = "Checkbox Example"

        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        SPracticePage = SP_MainPage(self.driver)
        ActCBText = SPracticePage.getCheckBoxTitle().text
        assert ActCBText == ExpCBText
        checkBoxs = SPracticePage.getCheckBoxes()
        for checkBox in checkBoxs:
            checkBox.click()
            assert checkBox.is_selected()

    def test_StaticDropDown_Handling(self):
        # variable
        ExpDDText = "Dropdown Example"

        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        SPracticePage = SP_MainPage(self.driver)
        ActDDTitle = SPracticePage.getDropDownTitle().text
        assert ActDDTitle == ExpDDText
        self.selectByVisibleText(SPracticePage.getDropDown(), "Option3")
        ActText = SPracticePage.getDropDown().get_attribute("value")
        assert ActText == "option3"

    def test_DynamicDropdwon_Handling(self):
        country = "Netherlands"
        ExpectedTitle = "Suggession Class Example"
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        sp_mainpage = SP_MainPage(self.driver)
        ActTitle = sp_mainpage.getDynamicDropdownTitle().text
        assert ActTitle == ExpectedTitle
        sp_mainpage.getdynDropdownTextBox().send_keys(country)
        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(sp_mainpage.dynamicDropdownOption(country)))
        sp_mainpage.getDynamicDropdownOption(country)
        assert country == sp_mainpage.getdynDropdownTextBox().get_attribute('value')
