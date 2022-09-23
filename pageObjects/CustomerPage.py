from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time




class AddCustomer:
    lnkCustomer_mainMenu_xpath = "//p[normalize-space()='Customers']//i[contains(@class,'right fas fa-angle-left')]"
    lnkCustomer_subMenu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    lnkAddNew_btn_xpath = "//a[normalize-space()='Add new']"
    txtCustEmail_xpath = "//input[@id='Email']"
    txtCustPassword_xpath = "//input[@id='Password']"
    txtCustFirstName_xpath = "//input[@id='FirstName']"
    txtCustLastName_xpath = "//input[@id='LastName']"
    txtDateofBirth_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtCustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstAdminstrators_xpath = "//li[normalize-space()='Administrators']"
    lstForumModerators_xpath = "//li[normalize-space()='Forum Moderators']"
    lstGuest_xpath = "//li[normalize-space()='Guests']"
    lstRegistered_xpath = "//li[normalize-space()='Registered']"
    lstVendors_xpath = "//li[contains(text(),'Vendors')]"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    drpMangerVendor_xpath = "//select[@id='VendorId']"
    chckActive_xpath = "//input[@id='Active']"
    chckTaxExempt_xpath = "//input[@id='Company']"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFemaleGender_xpath = "//input[@id='Gender_Female']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickMainCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_mainMenu_xpath).click()

    def clickSubCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_subMenu_xpath).click()

    def clickAddNew(self):
        self.driver.find_element(By.XPATH, self.lnkAddNew_btn_xpath).click()

    def addEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtCustEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtCustPassword_xpath).send_keys(password)

    def setFirstName(self, fName):
        self.driver.find_element(By.XPATH, self.txtCustFirstName_xpath).send_keys(fName)

    def setlastName(self, lName):
        self.driver.find_element(By.XPATH, self.txtCustLastName_xpath).send_keys(lName)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.rdFemaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()

    def setCompanyName(self, cName):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(cName)

    def taxExempt(self):
        self.driver.find_element(By.XPATH, self.chckTaxExempt_xpath).click()

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        time.sleep(5)

        if role == "Registered":
            self.listItem = self.driver.find_element(By.XPATH, self.lstRegistered_xpath)
            self.listItem.click()

        elif role == "Administrators":
            self.listItem = self.driver.find_element(By.XPATH, self.lstAdminstrators_xpath)
            self.listItem.click()

        elif role == "Forum Moderators":
            self.listItem = self.driver.find_element(By.XPATH, self.lstForumModerators_xpath)
            self.listItem.click()

        elif role == "Vendors":
            self.listItem = self.driver.find_element(By.XPATH, self.lstVendors_xpath)
            self.listItem.click()

        elif role == "Guests":
            time.sleep(5)
            self.listItem = self.driver.find_element(By.XPATH, self.lstGuest_xpath)
            self.listItem.click()
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()

        else:
            self.listItem = self.driver.find_element(By.XPATH, self.lstGuest_xpath)
            self.listItem.click()

    def setManagerofVendors(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpMangerVendor_xpath))
        drp.select_by_visible_text(value)

    def activeCustomer(self):
        self.driver.find_element(By.XPATH, self.chckActive_xpath).click()

    def addComment(self, comment):
        self.driver.find_element(By.XPATH, self.txtAdminComment_xpath).send_keys(comment)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
