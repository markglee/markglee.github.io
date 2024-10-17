
import unittest

def pangram (string) :
    alphabetstring = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    alphabet_list = alphabetstring.split()
    abc_copy = alphabet_list
    for y in alphabet_list :
        flag = 0
        for x in range (0, len(string)):
            if string[x] == y :
                abc_copy.remove(string[x])
                flag = 1
                break
        if flag :
            pass
        else : return False
    return True


        
class Pangram_Tests (unittest.TestCase) :

    def test_quick_brown_fox (self) :
        self.assertTrue(pangram('the quick brown fox jumps over the lazy dog'))

    def test_orange_fox (self) :
        self.assertFalse(pangram('the orange fox jumps over the lazy dog'))

unittest.main()
