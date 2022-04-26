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

    if number in (2, 3):
        return True

    if number == 1 or number % 2 == 0:
        return False

    exponent, power = find_exponent(number-1)

    for _ in range(iterations):
        base = random.randint(2, number-2)
        test_value = pow(base, exponent, number)
        if test_value not in (1, number-1):
            i = 1
            while i < power and test_value != number-1:
                test_value = pow(test_value, 2, number)
                if test_value == 1:
                    return False
                i += 1
            if test_value != number-1:
                return False

    return True


def extended_euclidean(number1, number2):
    """This function uses the extended Euclidean algorithm to calculate the greatest
       common divisor of the given numbers as well as the coefficients x and y
       such that x * number1 + y * number2 = gcd(number1, number2). Here, given that
       number1 and number2 are coprimes, x is the modular multiplicative inverse of
       number1 modulo number2, and it is used as the private key exponent.

    Args:
        number1: Integer value
        number2: Integer value

    Returns:
        A tuple of integers: (gcd, coefficient_x, coefficient_y)
    """

    if number1 == 0:
        return number2, 0, 1

    gcd, x1, y1 = extended_euclidean(number2 % number1, number1)

    coefficient_x = y1 - (number2 // number1) * x1
    coefficient_y = x1

    return (gcd, coefficient_x, coefficient_y)

def generate_primes(product_length=1024):
    """This function generates two probable prime numbers so that the bit length of their product is (around) the given length.

    Args:
        product_length: Integer value that defines the minimum length for the product of the generated primes.

    Returns:
        A list of two probable prime numbers.
    """

    primes = []
    variation = 3
    while len(primes) < 2:
        number = getrandbits(product_length // 2 + variation)
        if miller_rabin_primality_test(number) is False or number in primes:
            continue
        primes.append(number)
        variation = 5

    return primes

def create_keys(length=1024):
    """This function creates a key pair necessary for encryption and decryption.

    Args:
        length: Integer value that expresses the minimum key length in bits.

    Returns:
        A tuple containing the public key and the private key, ((modulus, public_exponent), (modulus, private_exponent)).
    """

    primes = generate_primes(length)
    modulus = primes[0] * primes[1]

    gcd = extended_euclidean(primes[0]-1, primes[1]-1)[0]
    lcm = abs((primes[0]-1) * (primes[1]-1)) // gcd

    public_exponent = 65537
    if public_exponent >= lcm or extended_euclidean(public_exponent, lcm)[0] != 1:

        while True:
            public_exponent = random.randint(2, lcm-1)
            if extended_euclidean(public_exponent, lcm)[0] == 1:
                break

    private_exponent = extended_euclidean(public_exponent, lcm)[1]

    return ((modulus, public_exponent), (modulus, private_exponent))
