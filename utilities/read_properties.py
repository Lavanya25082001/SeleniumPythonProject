import configparser



config=configparser.ConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url=config.get('admin login info','LaunchURL')
        return url

    @staticmethod
    def get_valid_username():
        username=config.get('admin login info','username')
        return username

    @staticmethod
    def get_valid_password():
        password=config.get('admin login info','password')
        return password

    @staticmethod
    def get_invalid_username():
        invalidUsername=config.get('admin login info','invalidUsername')
        return invalidUsername

    @staticmethod
    def get_invalid_password():
        invalidPassword=config.get('admin login info','invalidPassword')
        return invalidPassword