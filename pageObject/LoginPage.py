from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    userName = (By.CSS_SELECTOR, "[id='username']")
    password = (By.CSS_SELECTOR, "[id='password']")
    AdminRadioBtn = (By.CSS_SELECTOR, "input[value='admin']")
    UserRadioBtn = (By.CSS_SELECTOR, "input[value='user']")
    warningMsg = (By.CSS_SELECTOR, "[class='modal-body']")
    CancelBtn = (By.CSS_SELECTOR, "[id='cancelBtn']")
    OkayBtn = (By.CSS_SELECTOR, "[id='okayBtn']")
    UserTypeDrpdwn = (By.CSS_SELECTOR, "select[class='form-control']")
    IAgreeCheckbox = (By.CSS_SELECTOR, "[id='terms']")
    SignInBtn = (By.ID, "signInBtn")
    IncorrectMsg = (By.XPATH, "//form[@id='login-form']/div[contains(@class, 'alert-danger')]")

    def getusername(self):
        return self.driver.find_element(*LoginPage.userName)

    def getpassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getadminradiobtn(self):
        return self.driver.find_element(*LoginPage.AdminRadioBtn)

    def getuserradiobtn(self):
        return self.driver.find_element(*LoginPage.UserRadioBtn)

    def getwarningMsg(self):
        return self.driver.find_element(*LoginPage.warningMsg)

    def getCancelBtn(self):
        return self.driver.find_element(*LoginPage.CancelBtn)

    def getOkayBtn(self):
        return self.driver.find_element(*LoginPage.OkayBtn)

    def getUserTypeDropdown(self):
        return self.driver.find_element(*LoginPage.UserTypeDrpdwn)

    def getIAgreeCheckBox(self):
        return self.driver.find_element(*LoginPage.IAgreeCheckbox)

    def getSignInBtn(self):
        return self.driver.find_element(*LoginPage.SignInBtn)

    def getIncorrectMsg(self):
        return self.driver.find_element(*LoginPage.IncorrectMsg)