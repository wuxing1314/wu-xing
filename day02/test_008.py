'''
有多个fixture带参数

一个字符串的搜索功能，有三个输入
    要搜索的字符串：大写、小写、大小写混合；
    搜索的设置，是否区分大小写：是、否
    搜索的设置，所搜的方向，向上搜索、向下所搜。
'''
import pytest

# 要搜索的字符串
@pytest.fixture(params=['HELLO','Hello','hello'])
def zfc(request):
    return request.param

# 搜索的设置，所搜的方向，向上搜索、向下所搜。
@pytest.fixture(params=['向上','向下'])
def fx(request):
    return request.param

# 搜索的设置，是否区分大小写：是、否
@pytest.fixture(params=['是','否'])
def dx(request):
    return request.param

def test_search(zfc,fx,dx):
    print(f"测试搜索功能，搜索的字符串为：{zfc},所搜的方向为：{fx},是否区分大小写:{dx}")