from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("***** Test_002_DDT_Login *****")
        self.logger.info("***** Verifying Dashboard title DDT *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows: ", self.rows)

        self.cols = ExcelUtils.getColumnCount(self.path, 'Sheet1')
        print("Number of Cols: ", self.cols)

        # looping through rows
        lst_actResult = []  # empty list to store the status

        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserEmail(self.user)
            self.lp.setUserPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            # monitoring expected title and actual tile and user logging

            if exp_title == act_title:
                if self.exp == "Pass":
                    self.logger.info("***** Passed *****")
                    self.lp.clickLogout()
                    lst_actResult.append("Pass")


                elif self.exp == "Fail":
                    self.logger.error("***** Failed *****")
                    lst_actResult.append("Fail")
            elif exp_title != act_title:
                if self.exp == "Pass":
                    self.logger.info("***** Failed *****")
                    lst_actResult.append("Fail")


                elif self.exp == "Fail":
                    self.logger.error("***** Passed *****")
                    lst_actResult.append("Pass")

        if "Fail" not in lst_actResult:
            self.logger.info("***** DashBoard Title DDT test case passed")
            print(lst_actResult)
            self.driver.close()
            assert True

        else:
            self.logger.info("***** DashBoard Title DDT test case failed")
            print(lst_actResult)
            self.driver.close()
            assert False
