# http://osherove.com/tdd-kata-1/

import unittest, re

def addstring(string):

    start = re.match('//.\n', string)
    if start:
        char = start.group()[2:3]
        string = string.lstrip(start.group())
    else : char = ','
    
    list_of_strings = string.split(char)
    if len(string) :
        total = 0
        for string in list_of_strings:
            if '\n' in string :
                x = string.split('\n')
                for n in x :
                    n.strip('\n')
                    total += int(n)
            else:   total += int(string)
        return total
    else: return 0


class addstring_testcases (unittest.TestCase):

    def test_empty_string_is_0 (self) :
        self.assertEqual(addstring(''),0)

    def test_one_is_one(self):
        self.assertEqual(addstring('1'),1)

    def test_two_is_two(self):
        self.assertEqual(addstring('2'),2)

    def test_two_numbers(self):
        self.assertEqual(addstring('2,2'), 4)

    def test_five_numbers(self):
        self.assertEqual(addstring('2,3,4,5,6'), 20)

    def test_different_delimeters(self):
        self.assertEqual(addstring('2\n3,4,5,6'), 20)

    def test_newlines(self):
        self.assertEqual(addstring('2\n3\n4,5,6'), 20)

    def test_different_deliminator(self):
        self.assertEqual(addstring('//;\n1;2;3;4;5;6'), 21)
        


unittest.main()
