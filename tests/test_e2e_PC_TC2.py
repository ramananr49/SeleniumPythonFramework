import pytest
from selenium.webdriver.support.select import Select

from TestDatas.PC_HomePageTestData import PC_HomePageTestData
from Utilities.BaseClass import BaseClass
from pageObject.PC_HomePage import PC_HomePage


class Test_e2e_ProtoCommerce(BaseClass):

    def test_e2e_formSubmission(self, getData):
        #variables
        ExpSuccessMsg = "Success! The Form has been submitted successfully!."
        log = self.getLogger()

        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        log.info("Navigated to https://rahulshettyacademy.com/angularpractice/")
        homePage = PC_HomePage(self.driver)
        homePage.getNameField().send_keys(getData["Name"])
        log.info("Name field is filled with "+getData["Name"])
        homePage.getEmailField().send_keys(getData["Email"])
        log.info("Email field is filled with " + getData["Email"])
        homePage.getPasswordField().send_keys(getData["Password"])
        log.info("Password field is filled with " + getData["Password"])
        homePage.getIceCreamCheckBox().click()
        self.selectByVisibleText(homePage.getGenderDropDown(), getData["Gender"])
        log.info("Gender Dropdown is selected as " + getData["Gender"])
        homePage.getEmployedRadioBtn().click()
        homePage.getDateOfBirthField().send_keys(getData["DOB"])
        log.info("Date of Birth field is filled with " + getData["DOB"])
        homePage.getSubmitBtn().click()
        log.info("Submit button clicked successfully")
        ActText = homePage.getSuccessMsg().text
        log.info(ActText)
        print(ActText)
        assert ExpSuccessMsg in ActText
        if ExpSuccessMsg != ActText:
            log.error(ActText+" is not match with expected "+ExpSuccessMsg)
        elif ExpSuccessMsg in ActText:
            log.warning(ActText+" is actual message & Expected messgae is "+ExpSuccessMsg)

    @pytest.fixture(params=PC_HomePageTestData.test_HomePageTestData)
    def getData(self, request):
        return request.param
