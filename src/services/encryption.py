from hashlib import sha512
from random import choice, randrange


def byte_string_to_binary_string(byte_string):
    """This function turns a byte string into a binary string.

    Args:
        byte_string: A byte string to be converted into binary string.

    Returns:
        A string that has the bytes of the original string in binary form.
    """

    result = ""

    for byte in byte_string:
        bits = bin(byte)[2:]
        if len(bits) < 8:
            bits = "0" * (8 - len(bits)) + bits
        result += bits

    return result


def text_to_binary_string(text):
    """This function turns a plaintext message into a binary string.

    Args:
        text: String value that is to be converted into a binary string.

    Returns:
        String value representing the original text in binary form.
    """

    return byte_string_to_binary_string(text.encode("utf-8"))


def binary_string_to_text(binary_string):
    """This function turns a binary string into a plaintext message.

    Args:
        binary_string: A string consisting of 1's and 0's. Length should be divisible by 8.

    Returns:
        String value representing the binary string in plaintext form.
    """

    int_value = int(binary_string, 2)
    byte_value = int_value.to_bytes((int_value.bit_length() + 7) // 8, "big")

    return byte_value.decode()


def bitwise_xor(binary_str1, binary_str2):
    """This function executes a xor operation on two binary strings.

    Args:
        binary_str1, binary_str2: Two binary strings.

    Returns:
        A binary string that is the result of the xor operation.
    """

    difference = len(binary_str1) - len(binary_str2)
    if difference > 0:
        binary_str2 = "0" * difference + binary_str2
    elif difference < 0:
        binary_str1 = "0" * difference + binary_str1

    result = ""
    for index in range(len(binary_str1)):
        if binary_str1[index] != binary_str2[index]:
            result += "1"
        else:
            result += "0"

    return result


def add_padding(mod_len, message, rand_bits):
    """This function turns the un-padded plaintext message into padded plaintext.

    Args:
        mod_len: Integer value that is the bit length of the key modulus.
        message: String value that is the un-padded plaintext message.
        rand_bits: A random binary string that is the seed of the mask generating function.

    Returns:
        A string that is the padded message.
    """

    bin_message = text_to_binary_string(message)
    bin_message += "0" * (mod_len - len(bin_message) - len(rand_bits))
    mask1 = generate_mask(rand_bits, mod_len - len(rand_bits))
    result1 = bitwise_xor(bin_message, mask1)

    mask2 = generate_mask(result1, len(rand_bits))
    result2 = bitwise_xor(rand_bits, mask2)

    return result1 + result2


def generate_mask(seed, length):
    """This function generates a mask of given length to be used with padding.

    Args:
        seed: A random binary string that provides the seed for mask generation.
        length: An integer that is the intended length of the mask in bits and divisible by 8.

    Returns:
        A binary string of the requested length.
    """

    counter = 0
    byte_seed = seed.encode("utf-8")
    byte_string = b""

    while len(byte_string) < length // 8:
        byte_counter = str(counter).encode("utf-8")
        byte_string += sha512(byte_seed + byte_counter).digest()
        counter += 1

    return byte_string_to_binary_string(byte_string[:length // 8])


def remove_padding(message):
    """This function removes the padding from a decrypted message.

    Args:
        message: Binary string that is the decrypted message with padding.

    Returns:
        A binary string that is the original message.
    """

    # Not implemented yet

    return message


def generate_random_binary_string(length):
    """This function generates a random binary string of the given length.

    Args:
        legth: The desired length of the resulting binary string.

    Returns:
        A binary string of the given length.
    """

    values = ["0", "1"]
    result = ""

    for _ in range(length):
        result += choice(values)

    return result


def encrypt_message(message, key_modulus, key_exponent):
    """This function turns the plaintext message into ciphertext.

    Args:
        message: String value that is the message to be encrypted.
        key_modulus: Integer value that is the first element of the key.
        key_exponent: Integer value that is the second element of the key.

    Returns:
        A string that is the encrypted message.
    """

    mod_length = len(bin(key_modulus)[2:])
    message_length = len(text_to_binary_string(message))
    limit = mod_length - message_length
    seed = generate_random_binary_string(randrange(8, limit, 8))

    padded_message = add_padding(mod_length, message, seed)
    padded_int = int(padded_message, 2)

    encrypted_int = pow(padded_int, key_exponent, key_modulus)
    encrypted_bin = bin(encrypted_int)[2:]

    return encrypted_bin


def decrypt_message(ciphertext, key_modulus, key_exponent):
    """This function decrypts a message.

    Args:
        ciphertext: String value that is the encrypted message.
        key_modulus: Integer value that is the first element of the key.
        key_exponent: Integer value that is the second element of the key.

    Returns:
        String value that is the decrypted message.
    """

    ciphertext_int = int(ciphertext, 2)
    padded_int = pow(ciphertext_int, key_exponent, key_modulus)
    padded_bin = bin(padded_int)[2:]
    message_bin = remove_padding(padded_bin)
    message = binary_string_to_text(message_bin)

    return message
