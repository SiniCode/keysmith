from random import choice

def message_to_blocks(message):
    """This function enables encrypting longer messages by splitting it into blocks of 512 bits.

    Args:
        message: String value that is the original message.

    Returns:
        A list of binary strings, with the length of 512 bits each."""

    blocks = []

    for index in range(0, len(message), 16):
        if len(message) > index + 16:
            block = message[index:index + 16]
        else:
            block = message[index:]
        block_bin = text_to_binary_string(block)
        if len(block_bin) < 512:
            block_bin = "0" * (512 - len(block_bin)) + block_bin
        blocks.append(block_bin)

    return blocks


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
    byte_value = int_value.to_bytes(
        (int_value.bit_length() + 7) // 8, byteorder="big")

    return byte_value.decode()


def generate_random_binary_string(length=256):
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


def encrypt_message(message, key_mod, key_exp):
    """This function turns the plaintext message into ciphertext.

    Args:
        message: String value that is the plaintext message.
        key_mod: Integer value that is the encryption key modulus.
        key_exp: Integer value that is the encryption key exponent.

    Returns:
        String consisting of the encrypted blocks separated by "#".
    """

    message_blocks = message_to_blocks(message)

    encrypted_blocks = ""
    for block in message_blocks:
        padded_bin = add_padding(block)
        padded_int = int(padded_bin, 2)
        cipher_block = pow(padded_int, key_exp, key_mod)
        encrypted_blocks += str(cipher_block) + "#"

    return encrypted_blocks


def decrypt_message(ciphertext, key_mod, key_exp):
    """This function turns a ciphertext into plaintext message.

    Args:
        ciphertext: String that consists of the encrypted message blocks separated with "#".
        key_mod: Integer value that is the decryption key modulus.
        key_exp: Integer value that is the decryption key exponent.

    Returns:
        String value that is the decrypted message.
    """

    encrypted_blocks = ciphertext.split("#")

    message = ""
    for block in encrypted_blocks[0:-1]:
        padded_int = pow(int(block), key_exp, key_mod)
        padded_bin = bin(padded_int)
        unpadded_bin = padded_bin[2:len(padded_bin) - 256].lstrip("0")
        message += binary_string_to_text(unpadded_bin)

    return message

def add_padding(message):
    """This function adds a simple padding to the message.

    Args:
        message: Binary string that is the unpadded message.

    Returns:
        Binary string that is the padded message.
    """
    padded_message = message + generate_random_binary_string()
    return padded_message
