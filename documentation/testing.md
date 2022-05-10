# Testing

## Unit testing

The software has automated unit tests for the functions that are used in key creation, encryption and decryption.
Test coverage is 96 %.

![](./images/coverage_report.png)

### Running the tests

1. Install the necessary dependencies with the command before using the app / running the tests for the first time

```bash
poetry install
```

2. Run tests

```bash
poetry run invoke test
```

3. Create coverage report

```bash
poetry run invoke coverage-report
```

## Performance testing

Key creation is the most complex task of this software. The performance has been tested with 100 key pairs of 1024 and 2048 bits with the following results.

### 1024-bit keys:

| Creation time | Seconds |
|:--------------|:-------:|
| Average       | 0.238   |
| Minimum       | 0.073   |
| Maximum       | 0.624   |

### 2048-bit keys:

| Creation time | Seconds |
|:--------------|:-------:|
| Average       | 2.570   |
| Minimum       | 0.607   |
| Maximum       | 8.478   |

### Running the performance test 

You can repeat the performance test in the root directory with this command:

```bash
poetry run invoke performance-test
```

## Manual testing

In addition to automated tests, encryption and decryption have been tested manually with various input messages, and all bugs that were found have been fixed.
Also, to make sure that the function `generate_primes` generates actual prime numbers in key creation, a set of generated primes was checked with an independent [primality test tool](https://www.dcode.fr/primality-test).
