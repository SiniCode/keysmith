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
