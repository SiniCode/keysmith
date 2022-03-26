import random


def find_exponent(number):
    """This is a helper function for the Miller-Rabin primality test.
       The function finds integers m and p such that the given number = m * 2^p.

    Args:
        number: Integer value (the number tested for primality - 1).

    Returns:
        A tuple where the first value gives the exponent for the first test value in the primality test (m),
        and the second value determines the maximum number of iterations within each test round (p).
    """

    result = (1, 1)
    power = 1
    while True:
        if number % (2 ** power) != 0:
            break
        result = (number // (2 ** power), power)
        power += 1
    return result


def miller_rabin_primality_test(number, iterations=128):
    """This function is a probabilistic primality test for the given number.

    Args:
        number: Integer value to be tested.
        iterations: Integer value that defines the number of iterations.
                    The higher the value, the more reliable the result.

    Returns:
        True if the given number is (probably) a prime number, and
        False if it is not.
    """

    exponent, power = find_exponent(number-1)

    for i in range(iterations):
        base = random.randint(2, number-2)
        test_value = pow(base, exponent, number)
        if test_value not in (1, number-1):
            j = 1
            while j < power and test_value != number-1:
                test_value = pow(test_value, 2, number)
                if test_value == 1:
                    return False
                j += 1
            if test_value != number-1:
                return False

    return True


def create_keys(length=1024):
    """This function creates a key pair necessary for encryption and decryption.

    Args:
        length: Integer value that expresses the minimum key length in bits.

    Returns:
        A tuple containing the public key and the private key, ((modulus, public_exponent), (modulus, private_exponent)).
    """

    primes = []
    while len(primes) < 2:
        number = random.getrandbits(length)
        if number in (2, 3):
            primes.append(number)
            continue
        if number == 1 or number % 2 == 0:
            continue
        if miller_rabin_primality_test(number) is False:
            continue
        primes.append(number)

    modulus = primes[0] * primes[1]

    public_exponent = "TODO"

    private_exponent = "TODO"

    return ((modulus, public_exponent), (modulus, private_exponent))
