# ConvertingTime

A Python project for converting 12-hour time to 24-hour time.

## Description

This project provides a Python function to convert 12-hour time (e.g., "8:30 am" or "8:30 pm") to 24-hour time (e.g., "0830" or "2030"). The function takes an hour, minute, and period ("am" or "pm") as input and returns a four-digit string representing the time in 24-hour format.

## Features

- Convert 12-hour time to 24-hour time
- Easy-to-use Python function

## Prerequisites

1. Python (version 3.x)
2. Git (optional, for version control)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Shazz-Designing/ConvertingTime.git

2. Navigate to the project directory:

   ```bash
   cd ConvertingTime

3. Create and activate a virtual environment 

    ```bash
    python -m venv venv
    .\venv\Scripts\Activate   # On Windows

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt


## Usage

1. Import the convert_to_24_hour function from the modules.app module:

    ```python
    from modules.app import convert_to_24_hour

2. Use the function to convert 12-hour time to 24-hour time:

    ```python
    result = convert_to_24_hour(8, 30, "am")
    print(result)  # Output: "0830"


## Testing

Consider writing tests for your code using a testing framework like pytest. Organize your tests in a separate directory (e.g., tests/).

To run tests, use the following command:

    pytest


Contributing

Feel free to contribute to this project. Fork the repository, make your changes, and submit a pull reques


License
This project is licensed under the MIT License.