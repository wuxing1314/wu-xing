class TestRegister:

    def test_001(self):
        print("注册用例1")

    def test_002(self,db,login):  #类里这个用例执行前置
        print("注册用例2")

    def test_003(self):
        print("注册用例3")