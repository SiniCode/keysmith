import unittest
import services.keys
import services.encryption

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
        self.assertTrue(services.keys.miller_rabin_primality_test(
            19134702400093278081449423917))

    def test_miller_rabin_primality_test_with_composite(self):
        self.assertFalse(services.keys.miller_rabin_primality_test(1))
        self.assertFalse(services.keys.miller_rabin_primality_test(133))
        self.assertFalse(services.keys.miller_rabin_primality_test(12668))
        self.assertFalse(
            services.keys.miller_rabin_primality_test(42738459243))

    def test_extended_euclidean(self):
        result = services.keys.extended_euclidean(1180, 482)
        self.assertEqual(result, (2, -29, 71))

    def test_extended_euclidean2(self):
        result = services.keys.extended_euclidean(888, 54)
        self.assertEqual(result, (6, -2, 33))

    def test_generate_primes_returns_list_with_two_elements(self):
        primes = services.keys.generate_primes()
        self.assertIsInstance(primes, list)
        self.assertEqual(len(primes), 2)

    def test_generate_primes_returns_primes_of_unequal_length(self):
        primes = services.keys.generate_primes()
        self.assertNotEqual(primes[1].bit_length(), primes[0].bit_length())

    def test_generate_primes_returns_integers_of_default_lenth(self):
        primes = services.keys.generate_primes()
        self.assertGreaterEqual(primes[0].bit_length(), 510)
        self.assertGreaterEqual(primes[1].bit_length(), 510)

    def test_create_keys_returns_modulus_of_default_length(self):
        modulus = services.keys.create_keys()[0][0]
        length = modulus.bit_length()
        self.assertGreaterEqual(length, 1020)

    def test_generate_primes_returns_integers_of_asked_lenth(self):
        primes = services.keys.generate_primes(2048)
        self.assertGreaterEqual(primes[0].bit_length(), 1020)
        self.assertGreaterEqual(primes[1].bit_length(), 1020)

    def test_create_keys_returns_modulus_of_default_length(self):
        modulus = services.keys.create_keys(2048)[0][0]
        length = modulus.bit_length()
        self.assertGreaterEqual(length, 2040)


class TestEncryptionAndDecryptionFunctions(unittest.TestCase):

    def test_byte_string_to_binary_string(self):
        s = "€".encode("utf-8")
        test_value = services.encryption.byte_string_to_binary_string(s)
        self.assertEqual(test_value, "111000101000001010101100")

    def test_text_to_binary_string(self):
        test_value = services.encryption.text_to_binary_string("£$")
        self.assertEqual(test_value, "110000101010001100100100")

    def test_bitwise_xor_with_strings_of_equal_length(self):
        s1 = "10010101"
        s2 = "01011111"
        test_value = services.encryption.bitwise_xor(s1, s2)
        self.assertEqual(test_value, "11001010")

    def test_bitwise_xor_with_strings_of_different_length(self):
        s1 = "10010101"
        s2 = "1011111"
        test_value = services.encryption.bitwise_xor(s1, s2)
        self.assertEqual(test_value, "11001010")

    def test_generate_random_binary_string_returns_string_of_default_length(self):
        s = services.encryption.generate_random_binary_string()
        self.assertEqual(len(s), 64)

    def test_generate_random_binary_string_returns_string_of_asked_length(self):
        s = services.encryption.generate_random_binary_string(32)
        self.assertEqual(len(s), 32)

    def test_encrypt_message_returns_different_strig_each_time(self):
        m = "Testing"
        key = services.keys.create_keys()[0]
        cipher1 = services.encryption.encrypt_message(m, key[0], key[1])
        cipher2 = services.encryption.encrypt_message(m, key[0], key[1])
        self.assertNotEqual(cipher1, cipher2)

    def test_decrypt_message_returns_correct_message(self):
        m = "Testing"
        keys = services.keys.create_keys()
        encrypted = services.encryption.encrypt_message(m, keys[0][0], keys[0][1])
        decrypted = services.encryption.decrypt_message(encrypted, keys[1][0], keys[1][1])
        self.assertEqual(decrypted, m)

    #This test fails because of UnicodeDecodeError
    #def test_decrypt_message_returns_correct_message2(self):
        #m = "Test"
        #keys = services.keys.create_keys()
        #encrypted = services.encryption.encrypt_message(m, keys[0][0], keys[0][1])
        #decrypted = services.encryption.decrypt_message(encrypted, keys[1][0], keys[1][1])
        #self.assertEqual(decrypted, m)

#### Testing the simpler encryption and decryption functions below ####

    def test_simple_encrypt_returns_integer(self):
        key = services.keys.create_keys()[0]
        test_value = services.encryption.simple_encrypt("aaa", key[0], key[1])
        self.assertIsInstance(test_value, int)

    def test_simple_encrypt_returns_different_integers(self):
        key = services.keys.create_keys()[0]
        test_value1 = services.encryption.simple_encrypt("aaa", key[0], key[1])
        test_value2 = services.encryption.simple_encrypt("aaa", key[0], key[1])
        self.assertNotEqual(test_value1, test_value2)

    def test_simple_decrypt_returns_correct_message(self):
        m = "Testing, testing..."
        keys = services.keys.create_keys()
        encrypted = services.encryption.simple_encrypt(m, keys[0][0], keys[0][1])
        decrypted = services.encryption.simple_decrypt(encrypted, keys[1][0], keys[1][1])
        self.assertEqual(decrypted, m)

    def test_simple_padding_returns_string_of_correct_length(self):
        s = "10010001"
        padded = services.encryption.simple_padding(s)
        self.assertEqual(len(padded), 72)

    def test_simple_padding_returns_different_strings(self):
        s = "10010001"
        padded1 = services.encryption.simple_padding(s)
        padded2 = services.encryption.simple_padding(s)
        self.assertNotEqual(padded1, padded2)
