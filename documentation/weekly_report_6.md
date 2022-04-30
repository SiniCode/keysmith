# Weekly Report: Week 6

## Completed Tasks (18 hours)
* I did the peer review.
* I tried to make the oaep-padding work but decryption only succeeded with some inputs so I decided to settle for a simpler version.
* I added a function that splits the message into blocks to enable processing messages of greater bit-length than the key_modulus.
* I added encryption and decryption to gui.
* I wrote some tests.

## What next?
* I will complete the documentation.
* I will put final touches to gui.

## Questions
* I tried to write a [performance test](https://github.com/SiniCode/keysmith/blob/main/src/tests/performance_test.py) and include it in the src but importing the keys file does not work. Any ideas how to fix it?
