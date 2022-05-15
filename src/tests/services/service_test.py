import unittest
import services.keys
import services.encryption


class TestKeyCreationFunctions(unittest.TestCase):

    def test_find_exponent_returns_2_tuple_of_integers(self):
        result = services.keys.find_exponent(52)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], int)

    def test_find_exponent_returns_correct_result(self):
        result = services.keys.find_exponent(52)
        self.assertEqual(result, (13, 2))
        result = services.keys.find_exponent(220)
        self.assertEqual(result, (55, 2))

    def test_find_exponent_with_zero(self):
        result = services.keys.find_exponent(0)
        self.assertEqual(result, (0, 1))

    def test_miller_rabin_primality_test_returns_boolean(self):
        result = services.keys.miller_rabin_primality_test(109)
        self.assertIsInstance(result, bool)

    def test_miller_rabin_primality_test_with_prime(self):
        self.assertTrue(services.keys.miller_rabin_primality_test(2))
        self.assertTrue(services.keys.miller_rabin_primality_test(3))
        self.assertTrue(services.keys.miller_rabin_primality_test(109))
        self.assertTrue(services.keys.miller_rabin_primality_test(
            19134702400093278081449423917))

    def test_miller_rabin_primality_test_with_composite(self):
        self.assertFalse(services.keys.miller_rabin_primality_test(133))
        self.assertFalse(services.keys.miller_rabin_primality_test(12668))
        self.assertFalse(
            services.keys.miller_rabin_primality_test(42738459243))

    def test_miller_rabin_primality_test_with_non_prime(self):
        self.assertFalse(services.keys.miller_rabin_primality_test(0))
        self.assertFalse(services.keys.miller_rabin_primality_test(1))

    def test_miller_rabin_primality_test_with_procuct_of_big_primes(self):
        primes = services.keys.generate_primes()
        product = primes[0] * primes[1]
        self.assertFalse(services.keys.miller_rabin_primality_test(product))

    def test_extended_euclidean_returns_3_tuple_of_integers(self):
        result = services.keys.extended_euclidean(1180, 482)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], int)
        self.assertIsInstance(result[2], int)

    def test_extended_euclidean_returns_correct_result(self):
        result = services.keys.extended_euclidean(1180, 482)
        self.assertEqual(result, (2, -29, 71))
        result = services.keys.extended_euclidean(888, 54)
        self.assertEqual(result, (6, -2, 33))

    def test_extended_euclidean_with_zero_as_number1(self):
        result = services.keys.extended_euclidean(0, 9)
        self.assertEqual(result, (9, 0, 1))

    def test_generate_primes_returns_list_with_two_elements(self):
        primes = services.keys.generate_primes()
        self.assertIsInstance(primes, list)
        self.assertEqual(len(primes), 2)

    def test_generate_primes_returns_primes_of_unequal_length(self):
        primes = services.keys.generate_primes()
        self.assertNotEqual(primes[1].bit_length(), primes[0].bit_length())

    def test_generate_primes_returns_list_of_integers(self):
        primes = services.keys.generate_primes()
        self.assertIsInstance(primes[0], int)
        self.assertIsInstance(primes[1], int)

    def test_generate_primes_returns_primes(self):
        primes = services.keys.generate_primes()
        self.assertTrue(services.keys.miller_rabin_primality_test(primes[0]))
        self.assertTrue(services.keys.miller_rabin_primality_test(primes[1]))

    def test_generate_primes_returns_integers_with_default_product_length(self):
        primes = services.keys.generate_primes()
        product = primes[0] * primes[1]
        self.assertEqual(product.bit_length(), 1024)

    def test_generate_primes_returns_integers_with_asked_product_length(self):
        primes = services.keys.generate_primes(2048)
        product = primes[0] * primes[1]
        self.assertEqual(product.bit_length(), 2048)

    def test_create_keys_returns_2_tuple_of_2_tuples(self):
        keys = services.keys.create_keys()
        self.assertIsInstance(keys, tuple)
        self.assertEqual(len(keys), 2)
        self.assertIsInstance(keys[0], tuple)
        self.assertEqual(len(keys[0]), 2)
        self.assertIsInstance(keys[1], tuple)
        self.assertEqual(len(keys[1]), 2)

    def test_create_keys_returns_tuples_of_integers(self):
        keys = services.keys.create_keys()
        self.assertIsInstance(keys[0][0], int)
        self.assertIsInstance(keys[0][1], int)
        self.assertIsInstance(keys[1][0], int)
        self.assertIsInstance(keys[1][1], int)

    def test_create_keys_returns_modulus_of_default_length(self):
        modulus = services.keys.create_keys()[0][0]
        length = modulus.bit_length()
        self.assertGreaterEqual(length, 1020)

    def test_generate_primes_returns_integers_of_asked_lenth(self):
        primes = services.keys.generate_primes(2048)
        self.assertGreaterEqual(primes[0].bit_length(), 1020)
        self.assertGreaterEqual(primes[1].bit_length(), 1020)

    def test_create_keys_returns_modulus_of_asked_length(self):
        modulus = services.keys.create_keys(2048)[0][0]
        length = modulus.bit_length()
        self.assertGreaterEqual(length, 2040)


class TestEncryptionAndDecryptionFunctions(unittest.TestCase):

    def test_message_to_blocks_returns_512_bit_blocks(self):
        m = "a" * 300
        blocks = services.encryption.message_to_blocks(m)
        self.assertEqual(len(blocks[0]), 512)
        self.assertEqual(len(blocks[-1]), 512)

    def test_byte_string_to_binary_string(self):
        s = "€".encode("utf-8")
        test_value = services.encryption.byte_string_to_binary_string(s)
        self.assertEqual(test_value, "111000101000001010101100")

    def test_text_to_binary_string(self):
        test_value = services.encryption.text_to_binary_string("£$")
        self.assertEqual(test_value, "110000101010001100100100")

    def test_generate_random_binary_string_returns_string_of_default_length(self):
        s = services.encryption.generate_random_binary_string()
        self.assertEqual(len(s), 256)

    def test_generate_random_binary_string_returns_string_of_asked_length(self):
        s = services.encryption.generate_random_binary_string(64)
        self.assertEqual(len(s), 64)

    def test_encrypt_message_returns_different_ciphertexts_each_time(self):
        key = services.keys.create_keys()[0]
        test_value1 = services.encryption.encrypt_message(
            "aaa", key[0], key[1])
        test_value2 = services.encryption.encrypt_message(
            "aaa", key[0], key[1])
        self.assertNotEqual(test_value1, test_value2)

    def test_decrypt_message_returns_correct_short_message(self):
        m = "Testing, testing..."
        keys = services.keys.create_keys()
        encrypted = services.encryption.encrypt_message(
            m, keys[0][0], keys[0][1])
        decrypted = services.encryption.decrypt_message(
            encrypted, keys[1][0], keys[1][1])
        self.assertEqual(decrypted, m)

    def test_decrypt_message_returns_correct_long_message(self):
        m = "abcdE" * 100
        keys = services.keys.create_keys()
        encrypted = services.encryption.encrypt_message(
            m, keys[0][0], keys[0][1])
        decrypted = services.encryption.decrypt_message(
            encrypted, keys[1][0], keys[1][1])
        self.assertEqual(decrypted, m)

    def test_decrypt_message_with_special_characters(self):
        m = "¤%&*£$~^"
        keys = services.keys.create_keys()
        encrypted = services.encryption.encrypt_message(
            m, keys[0][0], keys[0][1])
        decrypted = services.encryption.decrypt_message(
            encrypted, keys[1][0], keys[1][1])
        self.assertEqual(decrypted, m)

    def test_decrypt_message_with_scandinavian_letters(self):
        m = "åäöÅÄÖ"
        keys = services.keys.create_keys()
        encrypted = services.encryption.encrypt_message(
            m, keys[0][0], keys[0][1])
        decrypted = services.encryption.decrypt_message(
            encrypted, keys[1][0], keys[1][1])
        self.assertEqual(decrypted, m)

    def test_decrypt_message_with_keys_swapped(self):
        m = "Test123!"
        keys = services.keys.create_keys()
        encrypted = services.encryption.encrypt_message(
            m, keys[1][0], keys[1][1])
        decrypted = services.encryption.decrypt_message(
            encrypted, keys[0][0], keys[0][1])
        self.assertEqual(decrypted, m)

    def test_add_padding_returns_string_of_correct_length(self):
        s = "10010001"
        padded = services.encryption.add_padding(s)
        self.assertEqual(len(padded), 264)

    def test_add_padding_returns_different_strings_each_time(self):
        s = "10010001"
        padded1 = services.encryption.add_padding(s)
        padded2 = services.encryption.add_padding(s)
        self.assertNotEqual(padded1, padded2)
