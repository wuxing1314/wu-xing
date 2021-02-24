"""
读数据
"""
import configparser
import os

import yaml


def get_project_path():
    """
    获取工程路径
    :return: D:\pythonProject\Zonghe\
    """
    # 当前文件目录
    file_path = os.path.realpath(__file__)
    print("当前文件所在目录：", file_path)
    # 上级目录
    dir_path = os.path.dirname(file_path)
    print("上级目录：",dir_path)
    # 再上一级
    dir_path = os.path.dirname(dir_path)
    print("再上目录：", dir_path)
    # 最后在拼一个
    return dir_path + "\\"

def read_ini(file_path, key):
    """
    读取配置文件
    :param file_path: 配置文件
    :param key: 配置文件中的key值
    :return: 返回key对应的value
    """
    # configparser内置的包，调用ini文件
    config = configparser.ConfigParser()
    file_path = get_project_path() + file_path
    config.read(file_path)
    # "env"对应ini文件的[env]
    value = config.get("env", key)
    return value

def read_yaml(file_path):
    '''
    读取yaml文件
    :param file_path: 文件路径
    :return: 文件内容
    '''
    file_path = get_project_path()+file_path
    # 只读方式打开文件
    with open(file_path,"r",encoding="utf8") as f:
        # 读文件
        file_content = f.read()
        # yaml自带load方法将文件转成列表
        content = yaml.load(file_content,Loader=yaml.FullLoader)
        return content


if __name__ == '__main__':
    a = read_ini(r"test_env/env.ini")
    print(a)

'''
[{
'data': {'mobilephone': 18012345678, 'pwd': ''}, 
'expect': {'status': 0, 'code': 20103, 'data': 'None', 'mag': '参数不能为空'}
}, 
{'data': {'mobilephone': 18012345678, 'pwd': '123456789012321312312312'}, 
'expect': {'status': 0, 'code': 20108, 'data': 'None', 'mag': '密码长度必须为6~18'}}]

'''
