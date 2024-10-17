import unittest


def adding(num1, num2):
    return num1 + 1

class adding_TestCase(unittest.TestCase):
    def test_oneplusone(self):
        self.assertEqual(adding(1,1),2)

    def test_eightistrue(self):
        self.assertTrue(adding(3,5))

    def test_zeroisfalse(self):
        self.assertFalse(adding(0,0))

unittest.main()

