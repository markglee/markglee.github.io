import unittest


def is_prime(number):
    for element in range (2,int(number + 1/2)):
        if number % element == 0:
            return False
    return True


def next_prime(number):
    while True:
        number += 1
        if is_prime(number): return (number)
 

    

class next_primesTestCase(unittest.TestCase):

   
    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_six_prime(self):
        self.assertFalse(is_prime(6))

    def test_next_prime_test(self):
        self.assertEqual(next_prime(54),59)
    

unittest.main()
