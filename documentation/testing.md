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

## Performance Testing

Key creation performance has been tested with 100 key pairs of 1024 and 2048 bits.

* The average 1024-bit key creation time was 0.32 seconds.
* The average 2048-bit key creation time was 2.99 seconds. 
