# main.py
from calculator import BasicCalculator
from helper_functions import greet_user

def main():
    calculator = BasicCalculator()

    # Perform some calculations
    result_add = calculator.add(5, 7)
    result_multiply = calculator.multiply(3, 4)

    # Display results and greet the user
    print(f"Result of addition: {result_add}")
    print(f"Result of multiplication: {result_multiply}")

    greet_user("John")

if __name__ == "__main__":
    main()
