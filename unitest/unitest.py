import unittest

from count import Count

class TestCount(unittest.TestCase):

    def setUp(self):
        #print('setUp')
        self.obj=Count()

    def tearDown(self):
        #print('tearDown')
        self.obj=None

    #use decorator to skip this test
    @unittest.skip(reason='No Test')
    def test_add(self):
        self.assertEqual(self.obj.add(10,20),30)

    #user decorator to skip low version
    #If the version retruns True,skip it
    @unittest.skipIf(Count.version==1.0,reason='Low version')
    def test_sub(self):
        self.assertEqual(self.obj.sub(10,6),4)

    #skip everything unless the version returns True
    @unittest.skipUnless(Count.version==1.5,reason='Low version')
    def test_sum(self):
        self.assertEqual(self.obj.add(10,3),13)

    #You expect it will fail,and you don't want it to report
    @unittest.expectedFailure
    def test_sum(self):
        self.assertEqual(self.obj.add(10,3),3)

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
        unittest.TestSuite. __init__(self,map(TestCount,case_list))


if __name__ == '__main__':
    #最簡單檢測的方式(須要以test開頭的方法)
    unittest.main()
    # s=get_suite()
    # #s=CountTestSuite()
    # runner=unittest.TextTestRunner()
    # print('Count of Case:',s.countTestCases())
    # runner.run(s)
