# Project Specification

## Goal

The goal is to produce an encryption application following the [RSA algorithm](https://en.wikipedia.org/wiki/RSA_(cryptosystem)).

## Features

The user can
* create secure encryption keys: each key must be at least 1024 bits long
* encrypt a message with a specified key
* decrypt a message with a specified key

There will be a simple graphical user interface to make it convenient for the user to create the keys and type their messages.

## Algorithms

### Miller-Rabin Primality Test 
The Miller-Rabin primality test is used in key creation. The public and private key have a common part, modulus, that has to be a product of two large prime numbers.
The test does not guarantee the primality of a number but the level of certainty is high enough for the purposes of this application.

### Extended Euclidean Algorithm
The extended Euclidean algorithm is also used in key creation when computing the public and private key exponent.
The algorithm calculates the greatest common divisor of two numbers, a and b, as well as the coefficients, x and y, such that ax + by = gcd(a,b).

## Requested Background Information

* Programming language: Python
* Documentation language: English 
* Study programme: Bachelor's Programme in Computer Science

## Sources

1. "[Extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)", 2021, *Wikipedia*, wiki article, viewed 15 May 2022.
2. "[Miller-Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)", 2022, *Wikipedia*, wiki article, viewed 15 May 2022. 
