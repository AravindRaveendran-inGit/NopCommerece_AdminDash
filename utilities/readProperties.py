import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('basic info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        useremail = config.get('basic info', 'useremail')
        return useremail

    @staticmethod
    def getPassword():
        password = config.get('basic info', 'password')
        return password