import unittest

from count import Count

class TestCount(unittest.TestCase):
    
    def setUp(self):
        print('setUp')
        self.obj=Count()

    def tearDown(self):
        print('tearDown')
        self.obj=None

    def add_test(self):
        print('runaddTest')
        print(self.obj.add(10,20)==30)
    
    def sub_test(self):
        print('runsubTest')
        print(self.obj.add(10,6)==4)
    
    # def runTest(self):
    #     print (self.obj.add(10,20)==30)

if __name__ == '__main__':
    demo_countadd=TestCount('add_test')
    demo_countadd.run()
    demo_countsub=TestCount('sub_test')
    demo_countsub.run()

