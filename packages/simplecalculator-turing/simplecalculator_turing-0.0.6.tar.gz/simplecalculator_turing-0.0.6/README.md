# **SimpleCalculator**
A simple command-line calculator program that can perform 
basic arithmetic operations and nth root calculation.

## Features
- Add, subtract, multiply, and divide numbers
- Calculate the nth root of a number
- Reset the calculator value to zero
- Validation for input numbers

## Installation
`pip install simplecalculator-turing==0.0.6`

## Usage
1. Run the program by running `simplecalculator` in your terminal
2. Follow the prompts to enter operations and numbers
3. Type 'exit' to quit the program

## Code Structure
- __init__: Initialize the calculator with an initial value of 0
- add: Add a number to the current value
- subtract: Subtract a number from the current value
- multiply: Multiply the current value by a number
- divide: Divide the current value by a number
- nth_root: Calculate the nth root of the current value
- reset: Reset the current value to 0
- _validate_number: Validate if the given value is a number (float or int)
- run: Run the calculator program until the user types 'exit'

## License
This program is distributed under the terms of the GNU General Public License v3.0. 
For more details, visit https://www.gnu.org/licenses/gpl-3.0.en.html#license-text

## Examples

To start the program type the below code in your command prompt or terminal.<br>
`simplecalculator`

You will receive the following prompt to select from one of the following commands:<br>
`Enter an operation to perform ('add', 'subtract', 'multiply', 'divide', 'nth_root', 'reset', or 'exit'):`

1. Type in one of the arithmetic operations:
`add`<br>
2. Select a number:
`Enter a number: 8`<br>
3. Receive the current value:
`The current value is: 8.0`
4. Type in one of the arithmetic operations:
`subtract`<br>
5. Select a number:
`Enter a number: 4`<br>
6. Receive the current value:
`The current value is: 4.0`

If you would like to **reset** the calculator to 0. Type in `reset`.
`The calculator has been reset to 0.`

If you would like to **quit** the calculator. Type in `exit`.
