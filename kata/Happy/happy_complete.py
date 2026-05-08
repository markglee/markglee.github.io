import unittest

def happy (x) :
    seen = []
    while x != 1:
        y = 0
        for n in range(len(str(x))):
            y += int(str(x)[n])**2
        if y in seen : return False
        seen.append(y)

        x = y
    return True
                    
                    
for x in range (1, 100) :
     if happy(x) : print (x, end = " ")


class happy_testcases(unittest.TestCase):
    def test_ten_is_a_happy_number(self) :
        self.assertTrue(happy(10))

    def test_nine_is_NOT_a_happy_number(self) :
        self.assertFalse(happy(9))

unittest.main()
