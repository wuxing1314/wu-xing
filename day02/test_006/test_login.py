class TestLogin:

    def test_001(self):
        print("登录用例1")

    def test_002(self,db,login):  # 类里这个用例执行前置
        print("登录用例2")

    def test_003(self):
        print("登录用例3")