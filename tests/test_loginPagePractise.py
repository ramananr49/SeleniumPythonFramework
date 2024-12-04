import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from TestDatas.LogInPageTestData import LogInPageTestData
from Utilities.BaseClass import BaseClass
from pageObject.LoginPage import LoginPage


class Test_LoginPagePractise(BaseClass):

    def test_valid_login(self, getdata):
        wait = WebDriverWait(self.driver, 5)
        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        loginPage = LoginPage(self.driver)
        loginPage.getusername().send_keys(getdata["username"])
        loginPage.getpassword().send_keys(getdata["password"])
        if getdata["user"] == "User":
            loginPage.getuserradiobtn().click()
            wait.until(expected_conditions.visibility_of_element_located(loginPage.warningMsg))
            ActWarningTxt = loginPage.getwarningMsg().text
            ExpWarningTxt = "You will be limited to only fewer functionalities of the app. Proceed?"
            assert ExpWarningTxt == ActWarningTxt
            loginPage.getOkayBtn().click()
        elif getdata["user"] == "Admin":
            loginPage.getadminradiobtn().click()
        self.selectByVisibleText(loginPage.getUserTypeDropdown(), getdata["userType"])
        loginPage.getIAgreeCheckBox().click()
        loginPage.getSignInBtn().click()
        ActTxt = loginPage.getSignInBtn().get_attribute("value")
        assert ActTxt == "Signing .."


    @pytest.fixture(params=LogInPageTestData.validTestData)
    def getdata(self, request):
        return request.param

    def test_invalid_login(self, getinvaliddata):
        wait = WebDriverWait(self.driver, 5)
        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        loginPage = LoginPage(self.driver)
        loginPage.getusername().send_keys(getinvaliddata["username"])
        loginPage.getpassword().send_keys(getinvaliddata["password"])
        loginPage.getuserradiobtn().click()
        wait.until(expected_conditions.visibility_of_element_located(loginPage.warningMsg))
        ActWarningTxt = loginPage.getwarningMsg().text
        ExpWarningTxt = "You will be limited to only fewer functionalities of the app. Proceed?"
        assert ExpWarningTxt == ActWarningTxt
        loginPage.getOkayBtn().click()
        self.selectByVisibleText(loginPage.getUserTypeDropdown(), getinvaliddata["userType"])
        loginPage.getIAgreeCheckBox().click()
        loginPage.getSignInBtn().click()
        wait.until(expected_conditions.visibility_of_element_located(loginPage.IncorrectMsg))
        assert loginPage.getIncorrectMsg().is_displayed()


    @pytest.fixture(params=LogInPageTestData.invalidTestData)
    def getinvaliddata(self, request):
        return request.param