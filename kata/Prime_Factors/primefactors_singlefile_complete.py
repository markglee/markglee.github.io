import unittest


def prime_factors_of(value) :
    if value < 2 : return []
    factor = 2

    while value % factor != 0 : factor += 1

    factors = [factor]
    factors.extend(prime_factors_of(value/factor))
    return factors

class TestPrimeFactors(unittest.TestCase):

    def setUp(self) :
        self.datas = [
                        [0,[]],
                        [1,[]],
                        [2,[2]],
                        [3,[3]],
                        [5,[5]],
                        [4, [2,2]],
                        [102, [2,3,17]]
                    ]

    def test_prime_factors_of_one(self):
        for data in self.datas:
            self.assertEqual(prime_factors_of(data[0]), data[1])

unittest.main()
