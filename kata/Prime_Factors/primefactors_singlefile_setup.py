import unittest




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
