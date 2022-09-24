import random
import string
import time
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.CustomerPage import AddCustomer
from selenium.webdriver.common.by import By

#To generate random sample emails.
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
class Test_003_addCustomer:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_addCustomer(self, setup):
        self.logger.info("***** Test_003_AddCustomer *****")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.lp.setUserEmail(self.useremail)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login Successful...")

        self.logger.info("***** Starting add customer test *****")

        self.addCustomer = AddCustomer(self.driver)
        self.addCustomer.clickMainCustomerMenu()
        time.sleep(5)
        self.addCustomer.clickSubCustomerMenu()
        self.addCustomer.clickAddNew()

        self.logger.info("***** Providing customer info *****")

        self.email = random_generator()+"@gmail.com"
        self.addCustomer.addEmail(self.email)
        self.addCustomer.setPassword("TestCase@0667")
        self.addCustomer.setFirstName("ZeroDimension")
        self.addCustomer.setlastName("Universe")
        self.addCustomer.setGender("Male")
        self.addCustomer.setCompanyName("Infinity Industries")
        self.addCustomer.taxExempt()
        self.addCustomer.setCustomerRoles("Guests")
        self.addCustomer.setManagerofVendors("Vendor 2")
        self.addCustomer.addComment("Busy in Learning...")
        self.addCustomer.clickSave()

        self.logger.info("***** Saving customer info *****")


        self.logger.info("***** Validating *****")

        self.Msg = self.driver.find_element(By.TAG_NAME,"body").text


        if 'The new customer has been added successfully.' in self.Msg:
            assert True
            self.logger.info("***** Add customer test case passed *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_error.png")
            self.logger.error("***** Add customer test case failed *****")
            assert False

        self.driver.close()


        self.logger.info("***** Ending Add Customer Test Case *****")







