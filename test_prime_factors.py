from unittest import TestCase
from prime_factors import PrimeFactor

class PrimeFactorTest(TestCase):
    def setUp(self):
        super().setUp()
        self.prime_factor = PrimeFactor()

    def test_prime_factor_of_1(self):
        self.assertEqual([], self.prime_factor.calcPrime(1))

    def test_prime_factor_of_2(self):
        self.assertEqual([2], self.prime_factor.calcPrime(2))

    def test_prime_factor_of_3(self):
        self.assertEqual([3], self.prime_factor.calcPrime(3))

    def test_prime_factor_of_4(self):
        self.assertEqual([2, 2], self.prime_factor.calcPrime(4))

    def test_prime_factor_of_6(self):
        self.assertEqual([2, 3], self.prime_factor.calcPrime(6))

    def test_prime_factor_of_9(self):
        self.assertEqual([3, 3], self.prime_factor.calcPrime(9))

    def test_prime_factor_of_12(self):
        self.assertEqual([2, 2, 3], self.prime_factor.calcPrime(12))