from selenium.webdriver.common.by import By


class PC_HomePage:

    def __init__(self, driver):
        self.driver = driver

    nameField = (By.XPATH, "//div[@class='form-group']//input[@name='name']")
    emailField = (By.XPATH, "//div[@class='form-group']//input[@name='email']")
    passwordField = (By.XPATH, "//div[@class='form-group']//input[@id='exampleInputPassword1']")
    iceCreamCheckBox = (By.CSS_SELECTOR, "input#exampleCheck1")
    genderDropDown = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    studentRadioBtn = (By.ID, "inlineRadio1")
    employedRadioBtn = (By.ID, "inlineRadio2")
    entrepreneurRadioBtn = (By.ID, "inlineRadio3")
    dateOfBirthField = (By.NAME, "bday")
    submitBtn = (By.CSS_SELECTOR, "input[type='submit']")
    sucessMsg = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def getNameField(self):
        return self.driver.find_element(*PC_HomePage.nameField)

    def getEmailField(self):
        return self.driver.find_element(*PC_HomePage.emailField)

    def getPasswordField(self):
        return self.driver.find_element(*PC_HomePage.passwordField)

    def getIceCreamCheckBox(self):
        return self.driver.find_element(*PC_HomePage.iceCreamCheckBox)

    def getGenderDropDown(self):
        return self.driver.find_element(*PC_HomePage.genderDropDown)

    def getStudentRadioBtn(self):
        return self.driver.find_element(*PC_HomePage.studentRadioBtn)

    def getEmployedRadioBtn(self):
        return self.driver.find_element(*PC_HomePage.employedRadioBtn)

    def getEntrepreneurRadioBtn(self):
        return self.driver.find_element(*PC_HomePage.entrepreneurRadioBtn)

    def getDateOfBirthField(self):
        return self.driver.find_element(*PC_HomePage.dateOfBirthField)

    def getSubmitBtn(self):
        return self.driver.find_element(*PC_HomePage.submitBtn)

    def getSuccessMsg(self):
        return self.driver.find_element(*PC_HomePage.sucessMsg)