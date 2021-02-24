'''
自定义标记：
    跳过用例：1、这个版本有缺陷，导致用例执行失败，缺陷修改周期较长，自动化通过率有一定的要求，
               为了不影响通过率，可以将失败的用例跳过，待缺陷解决后，在执行
               （@pytest.mark.skip）
            2、某个功能在最新版本V1R2实现，V1R2之前不支持
                （@pytest.mark.skipif）
    执行某一部分用例:界面、接口、功能、冒烟，脚本规模逐步增大，指向执行冒烟脚本的用例，
                  或者执行某个或者某几个接口用例，可以使用自定义标记
                  （@pytest.mark.自定义）
                  例如：smoke 表示 冒烟用例
                       func 表示 功能用例
                       api 表示 接口用例
'''
import pytest

Version = 'V1R2'

@pytest.mark.smoke
def test_001():
    print("用例1")

#跳过test_002
@pytest.mark.skip("跳过原因，由于xxxxx缺陷导致失败，该缺陷近期不解决")
def test_002():
    print("用例2")

@pytest.mark.skipif(Version != 'V1R2',reason='非V1R2版本不支持')
def test_003():
    print("用例3")

@pytest.mark.func  # 类里所有用例都有func标记
class TestMark:
    def test_004(self):
        print("用例4")

    @pytest.mark.smoke # 既有func标记，也有smoke标记
    def test_005(self):
        print("用例5")

    def test_006(self):
        print("用例6")

    def test_007(self):
        print("用例7")

    def test_008(self):
        print("用例8")
