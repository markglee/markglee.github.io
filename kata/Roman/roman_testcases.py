   
import unittest

def roman (number):
    roman_num = ''

    for x in range (number) : roman_num = roman_num + "I"
    
    return roman_num
    

class roman_numeral_testcases (unittest.TestCase) :

    def test_1_is_I(self):
        self.assertEqual(roman(1), 'I')
        
    def test_2_is_II(self):
        self.assertEqual(roman(2), 'II')

    def test_3_is_III(self):
        self.assertEqual(roman(3), 'III')
        
    def test_5_is_V(self):
        self.assertEqual(roman(5), 'V')

   

unittest.main()
