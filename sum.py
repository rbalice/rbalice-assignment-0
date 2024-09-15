def add_numbers(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        result = add_numbers(number1, number2)
        
        print(f"The sum of {number1} and {number2} is {result}.")
    except ValueError:
        print("Please enter valid numbers.")