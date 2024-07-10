from unittest import TestCase
from prime_factors import PrimeFactor

class PrimeFactorTest(TestCase):
    def test_prime_factor_of_1(self):
        prime_factor = PrimeFactor()
        self.assertEqual([], prime_factor.calcPrime(1))

    def test_prime_factor_of_2(self):
        prime_factor= PrimeFactor()
        self.assertEqual([2], prime_factor.calcPrime(2))