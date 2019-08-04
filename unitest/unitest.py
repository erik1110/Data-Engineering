import unittest

from count import Count

class TestCount(unittest.TestCase):
    
    def setUp(self):
        #print('setUp')
        self.obj=Count()

    def tearDown(self):
        #print('tearDown')
        self.obj=None

    def test_add(self):
        self.assertEqual(self.obj.add(10,20),30)
    
    def test_sub(self):
        self.assertEqual(self.obj.sub(10,6),4)

    def test_sum(self):
        pass

    def priv_case(self):
        pass

#自動生成測試集
def get_suite():
    suite=unittest.makeSuite(TestCount,prefix='test')
    suite.addTest(TestCount('priv_case'))
    print(suite.countTestCases())
    return suite

#單一生成測試集
# def get_suite():
#     demo_countadd=TestCount('add_test')
#     demo_countsub=TestCount('sub_test')
#     suite=unittest.TestSuite()
#     suite.addTest(demo_countadd)
#     suite.addTest(demo_countsub)
#     print(suite)
#     return suite

#使用__init__來構建測試案例集
class CountTestSuite(unittest.TestSuite):
    def __init__(self):
        case_list=['add_test','sub_test']
        unittest.TestSuite.__init__(self,map(TestCount,case_list))


if __name__ == '__main__':
    #最簡單檢測的方式(須要以test開頭的方法)
    unittest.main()
    # s=get_suite()
    # #s=CountTestSuite()
    # runner=unittest.TextTestRunner()
    # print('Count of Case:',s.countTestCases())
    # runner.run(s)
