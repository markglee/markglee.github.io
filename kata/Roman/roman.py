import unittest


def roman (input_number) :
    roman_numeral = ''
    numeral_lookup = {1000:'M', 500:'D',100:"C", 90:'XC',50:"C", 10:"X", 9:"IX",6:'VI',5:"V", 4:"IV", 1:'I'}
    special_numbers = list(numeral_lookup.keys())
    for number in special_numbers :
        occur, input_number = divmod(input_number, number)
        if occur :
            for i in range(occur):
                roman_numeral += numeral_lookup[number]
    return roman_numeral

    

class roman_numeral_testcases (unittest.TestCase) :

    def test_1_is_I(self):
        self.assertEqual(roman(1), 'I')

    def test_2_is_II(self):
        self.assertEqual(roman(2), 'II')

    def test_3_is_III(self):
        self.assertEqual(roman(3), 'III')

    def test_5_is_V(self):
        self.assertEqual(roman(5), 'V')

    def test_10_is_X(self):
        self.assertEqual(roman(10), 'X')

    def test_6_is_VI(self):
        self.assertEqual(roman(6), 'VI')

    def test_4_is_IV(self):
        self.assertEqual(roman(4), 'IV')

    def test_29_is_XXIX(self):
        self.assertEqual(roman(29), 'XXIX')

unittest.main()

    
        
