# Implementation

## Structure

### Services

All the functionality that the app provides is inside the [services](https://github.com/SiniCode/keysmith/tree/main/src/services) directory.
These services are further divided into
* key creation functions in the [keys.py](https://github.com/SiniCode/keysmith/blob/main/src/services/keys.py) file
* encryption and decryption functions in the [encryption.py](https://github.com/SiniCode/keysmith/blob/main/src/services/encryption.py) file.

#### Key creation

RSA key pair is asymmetric: the public and private key have a common *modulus*, and a unique *exponent*.
The modulus is a product of two large prime numbers. In this application, the default length of the modulus is around 1024 bits. 
The `create_keys` function first calls `generate_primes` fuction to calculate the modulus. To check the primality of the random numbers that `generate_primes` generates, it calls the `miller_rabin_primality_test` function.

The Miller-Rabin primality test is a probabilistic primality test, which means that the algorithm cannot guarantee that a number is a prime number, but that it is likely to be.
In this application, the default number of test rounds with different bases is 64, which means that the probability of mistaking a composite number for a prime is 1/4<sup>64</sup>.
The Miller-Rabin primality test is a polynomial-time algorithm, and its time complexity is O(*k*log<sup>3</sup>*n*), where *k* is the number of test rounds, and *n* is the number tested for primality.

The next step in key creation is to compute Carmichael's totient function of the modulus, λ(*n*), that is the least common multiple (lcm) of (*p* - 1) and (*q* - 1), where *p* and *q* are the generated primes.
To calculate this, `create_keys` calls the `extended_euclidean` function that calculates the greatest common divisor (gcd) of given numbers *a* and *b*, as well as the coefficients *x* and *y* such that *ax* + *by* = gcd(*a*, *b*).
Now, lcm(*a*, *b*) = |*ab*|/gcd(*a*, *b*), and the public exponent should be an integer between 1 and λ(*n*) such that gcd(*exponent*, λ(*n*)) = 1.
To improve efficiency, the public key exponent should have a small bit length and Hamming weight but not too small to compromise the security.
In this application, the default value for public key exponent is 2<sup>16</sup> + 1 = 65537, which is commonly used in RSA applications.

The private exponent, then, must be the modular multiplicative inverse of the public exponent modulo λ(*n*). It is also calculated with the `extended_euclidean` function.

#### Encryption

The `encrypt_message` function first calls `message_to_blocks` function that converts the message into binary form and splits it into 512-bit blocks.
Cutting up the message and encrypting it in blocks allows for processing also messages with greater bit-length than the key modulus.
For each block, `encrypt_message` calls the `add_padding` function that concatenates the block with 256 random bits. The idea of the padding is to provide protection against chosen plaintext attack.
Finally, the padded binary message is converted into an integer *m* and the ciphertext is calculated as *m* to the power of *e* modulo *n*, where *e* is the encryption key exponent and *n* is the key modulus.
The encrypted message consists of all the blocks concatenated with each other and separated by "#".

#### Decryption

The `decrypt_message` function first separates the blocks from each other and the decryption is executed block by block.
Now, the encrypted block is an integer *c*, and it is decrypted by calculating *c* to the power of *d* modulo *n*, where *d* is the decryption key exponent and *n* is the key modulus.
After decryption, the block is converted into binary form and the padding is removed. Finally, the binary string is converted into plaintext and all the blocks are concatenated together, giving the original message.

### User interface

The app has a simple graphical user interface that can be found in a separate directory, [ui](https://github.com/SiniCode/keysmith/tree/main/src/ui).
There are three different views that are all implemented as separate classes:
* `KeyCreationView` in [key_creation_view.py](https://github.com/SiniCode/keysmith/blob/main/src/ui/key_creation_view.py) file
* `EncryptionView` in [encryption_view.py](https://github.com/SiniCode/keysmith/blob/main/src/ui/encryption_view.py) file
* `DecryptionView` in [decryption_view.py](https://github.com/SiniCode/keysmith/blob/main/src/ui/decryption_view.py) file.

The `UI` class in [ui.py](https://github.com/SiniCode/keysmith/blob/main/src/ui/ui.py) file utilizes these classes and shows one of the views at a time.

## Shortcomings

The padding system used in this application is very simple and does not provide the same security level as Optimal Asymmetric Encryption Padding (OAEP) that should be used with RSA to prevent sophisticated attacks.
In addition, the graphical user interface has been implemented mainly for testing the functionalities. It is visually dull and lacks many features that would make it more convenient for the user, e.g., a scroll bar and the possibility to choose the length of the keys.

## Sources

1. "[Extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)", 2021, *Wikipedia*, wiki article, viewed 12 May 2022.
2. "[Miller-Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)", 2022, *Wikipedia*, wiki article, viewed 12 May 2022.
3. "[Miller-Rabin Primality Test](https://www.youtube.com/watch?v=qdylJqXCDGs)", 2016, *YouTube*, video, viewed 12 May 2022.
4. "[Primality Test | Set 3 (Miller-Rabin)](https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/)", 2022, *GeeksforGeeks*, online article, viewed 12 May 2022.
5. Prudhomme, Antoine 2018, "[How to generate big prime numbers - Miller-Rabin](https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb)", *Medium*, online article, viewed 12 May 2022.
6. "[Python Program for Extended Euclidean algorithms](https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/)", 2020, *GeeksforGeeks*, online article, viewed 12 May 2022.
7. "[RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))", 2022, *Wikipedia*, wiki article, viewed 12 May 2022.
8. "[The Extended Euclidean Algorithm](https://www.youtube.com/watch?v=hB34-GSDT3k)", 2014, *YouTube*, video, viewed 12 May 2022.
