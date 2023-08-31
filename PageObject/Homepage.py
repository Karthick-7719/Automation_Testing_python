from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.XPATH, "//label[text()='Name']/following-sibling::input")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    gender = (By.ID, "exampleFormControlSelect1")
    checkbox = (By.ID, "exampleCheck1")
    employeeStatus = (By.ID, "inlineRadio2")
    dob = (By.CSS_SELECTOR, "input[type='date']")
    submit = (By.XPATH, "//input[@value='Submit']")
    msgSuccess = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItem(self):
        return self.driver.find_element(*Homepage.shop)

    def getName(self):
        return self.driver.find_element(*Homepage.name)

    def getEmail(self):
        return self.driver.find_element(*Homepage.email)

    def getPassword(self):
        return self.driver.find_element(*Homepage.password)

    def getGender(self):
        return self.driver.find_element(*Homepage.gender)

    def getCheckbox(self):
        return self.driver.find_element(*Homepage.checkbox)

    def getEmployeeStatus(self):
        return self.driver.find_element(*Homepage.employeestatus)

    def getDob(self):
        return self.driver.find_element(*Homepage.dob)

    def getSubmit(self):
        return self.driver.find_element(*Homepage.submit)

    def getMsgSuccess(self):
        return self.driver.find_element(*Homepage.msgSuccess)
