# Cron Parser

## Overview
This is a command-line application that parses a cron string and expands each field to show the times at which it will run. The program supports the standard cron format with five time fields:

- **minute** (0-59)
- **hour** (0-23)
- **day of month** (1-31)
- **month** (1-12)
- **day of week** (1-7, where 1 is Monday and 7 is Sunday)
- **year** (2025-3000 , this is optional field)
- **command** (The command to execute)
- **command parameters** (Optional command parameters)

## Features
- Parses a cron expression and expands each field.
- Outputs a formatted table showing the expanded values.
- Supports `*`, `,`, `-`, and `/` operators.
- Includes an automated test suite.

## Usage
### Running the Program
Execute the program from the command line by passing a cron expression as an argument:

```sh
$ python -m cron_parser.main "*/15 0 1,15 * 1-5 /usr/bin/find"
```

### Example Output
For the input:
```sh
$ python -m cron_parser.main "*/15 0 1,15 * 1-5 /usr/bin/find"
```
The output will be:
```
minute         0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find
```

## Installation
### Prerequisites
- Python 3.x


## Running Tests
This project includes an automated test suite using `pytest`.
To run the tests, install `pytest` (if not already installed):

```sh
pip install pytest
```
Then run the tests:
```sh
pytest
```

## Implementation Details
### Parsing Logic
1. **Tokenization**: Splits the input cron expression into individual fields.
2. **Validation**: Ensures the correct number of fields and valid syntax.
3. **Parsing Tokens**:
   - `*` expands to the full range of values.
   - `,` allows specifying multiple values.
   - `-` defines a range of values.
   - `/` specifies step increments.
4. **Formatting Output**: Converts parsed values into a formatted table.

## Extensibility
The code is designed following SOLID principles:
- **Single Responsibility Principle**: Each class handles a distinct function (tokenization, parsing, validation).
- **Factory Pattern**: The `CronTokenFactory` is used to create appropriate token handlers, allowing easy extension. (Can be changed to registery modle instead of if else)
- **Open/Closed Principle**: New token types can be added without modifying existing parsing logic.

## Future Improvements
- Support for more complex cron syntax variations.