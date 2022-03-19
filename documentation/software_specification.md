# Software Specification

## Goal

The goal is to produce an encryption application following the [RSA algorithm](https://en.wikipedia.org/wiki/RSA_(cryptosystem)).

## Features

The user can
* create secure encryption keys: each key must be a prime number and at least 1024 bits long
* encrypt a message with a specified key
* decrypt a message with a specified key

There will be a simple graphical user interface to make it convenient for the user to create the keys and type their messages.

## Algorithms and Data Structures (incomplete)

### Miller-Rabin Primality Test 
[Miller-Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) is used to check the keys.
The test does not guarantee the primality of a number but the level of certainty is high enough for the purposes of this application.

## Requested Background Information

* Programming language: Python
* Documentation language: English 
* Study programme: Bachelor's Programme in Computer Science
