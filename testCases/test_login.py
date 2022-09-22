from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def testHomePageTitle(self, setup):
        self.logger.info("***** Started *****")
        self.logger.info("***** Verifying Home page title *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("***** Home page title test passed *****")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "testHomePageTitle.png")
            self.driver.close()
            self.logger.error("***** Home page title test failed *****")
            assert False

    def test_login(self, setup):
        self.logger.info("***** Verifying Dashboard title *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserEmail(self.useremail)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("***** Dashboard title test passed *****")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("***** Dashboard title test failed *****")
            assert False



