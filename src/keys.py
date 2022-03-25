import random


def miller_rabin_primality_test(number, iterations):
    """This function is a probabilistic primality test for the given number.

    Args:
        number: Integer value to be tested
        iterations: Integer value that defines the number of iterations.
                    The higher the value, the more reliable the result.

    Returns:
        True if the given number is (probably) a prime number, and
        False if it is not.
    """



def create_keys(length):
    """This function creates a key pair necessary for encryption and decryption.

    Args:
        length: Integer value that expresses the minimum key length in bits

    Returns:
        A tuple containing the public key and the private key, ((modulus, public_exponent), (modulus, private_exponent))
    """

    primes = []
    while len(primes) < 2:
        number = random.getrandbits(length)
        if number == 1 or number % 2 == 0:
            continue
        if miller_rabin_primality_test(number) == False:
            continue
        primes.append(number)

    modulus = primes[0] * primes[1]

    public_exponent = "TODO"

    private_exponent = "TODO"

    return (public_key, private_key)
