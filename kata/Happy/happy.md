## Happy Numbers

A happy number is calculated as follows:

23 -> 2^2 3^2 -> 4 + 9 -> 13
13 -> 1^2 3^2 -> 1 + 9 -> 10
10 -> 1^2 0^2 -> 1 + 0 -> 1

i.e. squaring the digits and then summing the result eventually reduces to 1.

# happy(x)

write a function which takes an integer and returns True if the integer is happy and false if not.

>>> happy(23)
True
>>> happy(11)
False

To help you I've provided some unit tests.

class happy_testcases(unittest.TestCase):
    def test_ten_is_a_happy_number(self) :
        self.assertTrue(happy(10))

    def test_nine_is_NOT_a_happy_number(self) :
        self.assertFalse(happy(9))

unittest.main()

## Lesson
*Think before you code!* 
What haven't I told you? Do you always need to understand a problem fully before writing code?