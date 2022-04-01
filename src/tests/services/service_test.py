import unittest
from sys import getsizeof
import services.keys

class TestKeyCreationFunctions(unittest.TestCase):

    def test_find_exponent(self):
        result = services.keys.find_exponent(52)
        self.assertEqual(result, (13, 2))

    def test_find_exponent2(self):
        result = services.keys.find_exponent(220)
        self.assertEqual(result, (55, 2))

    def test_miller_rabin_primality_test_with_prime(self):
        self.assertTrue(services.keys.miller_rabin_primality_test(2))
        self.assertTrue(services.keys.miller_rabin_primality_test(109))
        self.assertTrue(services.keys.miller_rabin_primality_test(19134702400093278081449423917))

    def test_miller_rabin_primality_test_with_composite(self):
        self.assertFalse(services.keys.miller_rabin_primality_test(1))
        self.assertFalse(services.keys.miller_rabin_primality_test(133))
        self.assertFalse(services.keys.miller_rabin_primality_test(12668))
        self.assertFalse(services.keys.miller_rabin_primality_test(42738459243))

    def test_extended_euclidean(self):
        result = services.keys.extended_euclidean(1180, 482)
        self.assertEqual(result, (2, -29, 71))

    def test_extended_euclidean2(self):
        result = services.keys.extended_euclidean(888, 54)
        self.assertEqual(result, (6, -2, 33))

    def test_create_keys_returns_modulus_of_correct_length(self):
        modulus = services.keys.create_keys()[0][0]
        length = getsizeof(modulus)*8
        self.assertGreaterEqual(length, 1024)
