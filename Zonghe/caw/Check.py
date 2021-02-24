import pytest as check

def equal(real,expect,keys):
    """
    将
    assert q.json()['code'] == login_data['expect']['code']
    assert q.json()['status'] == login_data['expect']['status']
    assert q.json()['msg'] == login_data['expect']['msg']
    简化为
    assert
    不推荐直接用字典判等，
        1、结果中有时间戳，每次实际结果都在变化
        2、实际结果中不是关键的信息，后期变化影响断言
        3、实际结果很长，预期结果很难写
    :param real: 实际结果--q.json()
    :param expect: 预期结果--login_data['expect']
    :param keys: 校验的关键字--code,status,msg
    :return:
    """
    ks = keys.split(",") # 字符串在“，”除切割
    for k in ks:
        r = str(real.get(k))
        e = str(expect.get(k))
        try:
            check.equal(r,e)
            print(f"检验{k}成功")
        except Exception as e:
            print(f"检验{k}失败")



