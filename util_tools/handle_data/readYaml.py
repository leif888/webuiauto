import yaml

from util_tools.logs_util.recordlog import logs


def read_yaml(file_path):
    """
    读取yaml文件的数据
    :param file_path: yaml文件路径
    :return: 返回列表类型，列表里面是元组数据，如：[('admin123','123456'),(),(),.....]
    """
    try:
        data_list_tuple = []
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            for data_str in data:
                if data_str is not None:
                    data_tuple = tuple(data_str.split(','))
                    data_list_tuple.append(data_tuple)
        return data_list_tuple
    except Exception as e:
        logs.error(f'读取yaml文件异常，异常原因为：{e}')
