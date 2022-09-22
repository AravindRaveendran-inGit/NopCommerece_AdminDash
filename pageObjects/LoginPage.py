from selenium.webdriver.common.by import By


class Login:
    textbox_useremail_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    button_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver


    def setUserEmail(self, useremail):
        self.driver.find_element(By.ID, value= self.textbox_useremail_id).clear()
        self.driver.find_element(By.ID, value= self.textbox_useremail_id).send_keys(useremail)

    def setUserPassword(self, password):
        self.driver.find_element(By.ID, value=self.textbox_password_id).clear()
        self.driver.find_element(By.ID, value=self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, value= self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, value=self.button_logout_linktext).click()
