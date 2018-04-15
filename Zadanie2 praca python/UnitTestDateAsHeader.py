import unittest
from Data import IfStringLooksLikeDate, IsHeaderDate
class Test_TestDateAsHeader(unittest.TestCase):
    def test_IfStringLooksLikeDate(self):
        ret=IfStringLooksLikeDate('01.01.2017')
        self.assertEqual(ret,True)

        ret=IfStringLooksLikeDate('31.12.2014')
        self.assertEqual(ret,True)

        ret=IfStringLooksLikeDate('00.00.2014')
        self.assertEqual(ret,False)

        ret=IfStringLooksLikeDate('32.01.2017')
        self.assertEqual(ret,False)

        ret=IfStringLooksLikeDate('15.13.2017')
        self.assertEqual(ret,False)

        ret=IfStringLooksLikeDate('15.13.1111')
        self.assertEqual(ret,False)

        ret=IfStringLooksLikeDate('15.13-2000')
        self.assertEqual(ret,False)

        ret=IfStringLooksLikeDate('15')
        self.assertEqual(ret,False)

        ret=IfStringLooksLikeDate('asdfghjkl;')
        self.assertEqual(ret,False)

    def test_IsHeaderDate(self):
        ret=IsHeaderDate('01.01.2017-15.01.2017')
        self.assertEqual(ret,True)

        ret=IsHeaderDate('01.01.201a-15.01.2017')
        self.assertEqual(ret,False)

        ret=IsHeaderDate('01.01.2015:15.01.2017')
        self.assertEqual(ret,False)

        ret=IsHeaderDate('gdfafadsd')
        self.assertEqual(ret,False)
        

if __name__ == '__main__':
    unittest.main()
