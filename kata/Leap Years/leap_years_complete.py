import unittest


class LeapTestCase(unittest.TestCase):
    def test_1990_is_not_leap(self):
        self.assertFalse(leap(1990))
    def test_2000_is_leap(self):
        self.assertTrue(leap(2000))
    def test_1928_is_leap(self) :
        self.assertTrue(leap(1928)) 
    def test_2024_is_leap(self) :
        self.assertTrue(leap(2024))
    def test_1900_is_not_leap(self) :
        self.assertFalse(leap(1900))

#https://kalender-365.de/leap-years.php
#If year can be evenly divided by 4; then it's a leap year
#unless it can be evenly divided by 100
#unless;
#The year is also evenly divisible by 400. Then it is a leap year.

def leap(year) :
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0 :
                return True
            else : return False
        else : return True
    else : return False
    

unittest.main()
