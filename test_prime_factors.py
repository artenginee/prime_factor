import unittest

from prime_factors import PrimeFactors


class MyTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.prime_factors = PrimeFactors()

    def test_prime_factors_of_1(self):
        self.assertEqual([], self.prime_factors.of(1))

    def test_prime_factors_of_2(self):
        self.assertEqual([2], self.prime_factors.of(2))

    def test_prime_factors_of_3(self):
        self.assertEqual([3], self.prime_factors.of(3))

if __name__ == '__main__':
    unittest.main()
