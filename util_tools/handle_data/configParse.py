import configparser

from config.setting import FILE_PATH
from util_tools.logs_util.recordlog import logs


class ConfigParse:
    """
    解析.ini配置文件
    """

    def __init__(self, file_path=FILE_PATH['ini']):
        self.config = configparser.ConfigParser()
        self.file_path = file_path
        self.read_config()

    def read_config(self):
        self.config.read(self.file_path)

    def get_value(self, section, option):
        try:
            value = self.config.get(section, option)
            return value
        except Exception as e:
            logs.error(f'解析配置文件出现异常，原因：{e}')

    def get_host(self, option):
        return self.get_value('HOST', option)

    def get_section_mysql(self, option):
        return self.get_value('MYSQL', option)
