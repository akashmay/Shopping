import configparser
import os.path

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.path.curdir)+"\\configurations\\config.ini")

class ReadProperties:
    @staticmethod
    def read_base_url():
        url = config.get(section="loginInfo",option="base_url")
        return url.replace('"',"")

    @staticmethod
    def read_excel_created_accounts_path():
        path = config.get(section="excelInfo",option="path_created_accounts")
        return path.replace('"',"")