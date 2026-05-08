import unittest

def happy (x) :
    pass
                    
                   
for x in range (1, 100) :
     if happy(x) : print (x, end = " ")


class happy_testcases(unittest.TestCase):
    def test_ten_is_a_happy_number(self) :
        self.assertTrue(happy(10))

    def test_nine_is_NOT_a_happy_number(self) :
        self.assertFalse(happy(9))

unittest.main()
