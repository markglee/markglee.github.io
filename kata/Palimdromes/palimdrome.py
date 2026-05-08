
import unittest



        
class Pangram_Tests (unittest.TestCase) :

    def test_quick_brown_fox (self) :
        self.assertTrue(pangram('the quick brown fox jumps over the lazy dog'))

    def test_orange_fox (self) :
        self.assertFalse(pangram('the orange fox jumps over the lazy dog'))

unittest.main()
