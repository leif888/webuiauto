import json

from util_tools.logs_util.recordlog import logs


def read_json(file_path):
    """
    读取json的数据
    :param file_path: 文件路径
    :return: 返回列表类型，列表里面是元组数据，如：[('admin123','123456'),(),(),.....]
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            data_list_tuple = [tuple(data_dict.values()) for data_dict in data]

        return data_list_tuple
    except Exception as e:
        logs.error(f'读取Json文件异常，异常原因为：{e}')
