print('''
SimpleCalculator  Copyright (C) 2024  Armin Rocas
This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it
under certain conditions; For more details, visit https://www.gnu.org/licenses/gpl-3.0.en.html#license-text
''')

class Calculator:
    """
    A calculator class that can perform basic arithmetic operations.
    """

    def __init__(self):
        """
        Initialize the calculator with an initial value of 0.
        """
        self.calculator_value = 0

    def add(self, number_to_add: float) -> None:
        """
        Add a number to the current value.

        Parameters:
        number_to_add (float): The number to add to the current value.
        """
        if self._validate_number(number_to_add):
            self.calculator_value += number_to_add
            print(f'The current value is: {self.calculator_value}')
        else:
            print(f'{number_to_add} is not a valid number.')

    def subtract(self, number_to_subtract: float) -> None:
        """
        Subtract a number from the current value.

        Parameters:
        number_to_subtract (float): The number to subtract from the current value.
        """
        if self._validate_number(number_to_subtract):
            self.calculator_value -= number_to_subtract
            print(f'The current value is: {self.calculator_value}')
        else:
            print(f'{number_to_subtract} is not a valid number.')

    def multiply(self, number_to_multiply_by: float) -> None:
        """
        Multiply the current value by a number.

        Parameters:
        number_to_multiply_by (float): The number to multiply the current value by.
        """
        if self._validate_number(number_to_multiply_by):
            self.calculator_value *= number_to_multiply_by
            print(f'The current value is: {self.calculator_value}')
        else:
            print(f'{number_to_multiply_by} is not a valid number.')

    def divide(self, number_to_divide_by: float) -> None:
        """
        Divide the current value by a number.

        Parameters:
        number_to_divide_by (float): The number to divide the current value by.
        """
        if self._validate_number(number_to_divide_by):
            try:
                if number_to_divide_by != 0:
                    self.calculator_value /= number_to_divide_by
                    print(f'The current value is: {self.calculator_value}')
                else:
                    raise ZeroDivisionError('Error: Cannot divide by zero.')
            except ZeroDivisionError as zd_error:
                print(zd_error)
        else:
            print(f'{number_to_divide_by} is not a valid number.')

    def nth_root(self, number_nth_root: float) -> None:
        """
        Calculate the nth root of the current value.
    
        Parameters:
        number_nth_root (float): The degree of the root to be calculated.
        """
        if self._validate_number(number_nth_root):
            try: 
                if self.calculator_value > 0 and number_nth_root != 0:
                    self.calculator_value **= (1/number_nth_root)
                    print(f'The current value is: {self.calculator_value}')
                else:
                    raise ValueError('Error: Cannot calculate root of 0.')
            except ValueError as v_error:
                print(v_error)
        else:
            print(f'{number_nth_root} is not a valid number.')

    def reset(self) -> None:
        """
        Reset the current value to 0.
        """
        self.calculator_value = 0
        print("The calculator has been reset to 0.")

    def _validate_number(self, value: float) -> bool:
        """
        Validate if the given value is a number (float or int).

        Parameters:
        value (float): The value to be validated.

        Returns:
        bool: True if the value is a number, False otherwise.
        """
        return isinstance(value, (float, int))

    def run(self):
        """
        Run the calculator program until the user types 'exit'.
        """
        while True:
            user_input = input("Enter an operation to perform ('add', 'subtract', 'multiply', 'divide', 'nth_root', 'reset', or 'exit'): ")
            if user_input.lower() == 'exit':
                break
            elif user_input.lower() == 'reset':
                self.reset()
            elif user_input.lower() in ['add', 'subtract', 'multiply', 'divide', 'nth_root']:
                try:
                    user_number = float(input("Enter a number: "))
                    if user_input.lower() == 'add':
                        self.add(user_number)
                    elif user_input.lower() == 'subtract':
                        self.subtract(user_number)
                    elif user_input.lower() == 'multiply':
                        self.multiply(user_number)
                    elif user_input.lower() == 'divide':
                        self.divide(user_number)
                    elif user_input.lower() == 'nth_root':
                        self.nth_root(user_number)
                except ValueError:
                    print('Invalid input. Please enter a number.')
            else:
                print('Invalid operation. Please choose from the provided options.')


def main():
    """"
    Create an instance and run the calculator.
    """
    calculator = Calculator()
    calculator.run()


if __name__ == '__main__':
    """"
    Run the main() function when the script is executed directly.
    """
    main()
