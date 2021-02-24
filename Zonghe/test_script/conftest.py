"""
脚本层的公共前置、后置，整个过程执行一次
不用import，通过conftest文件名来找到
"""

import pytest

from Zonghe.caw import DataRead
from Zonghe.caw.BaseRequests import BaseRequests


@pytest.fixture(scope='session')
def url():
    return DataRead.read_ini(r"test_env\env.ini", "url")


@pytest.fixture(scope='session')
def db_info():
    # ini读出来是字符串，但是db_info是字典，使用eval解析为原文本格式
    return eval(DataRead.read_ini(r"test_env\env.ini", "db_info"))


@pytest.fixture(scope='session')
def baserequest():
    return BaseRequests()