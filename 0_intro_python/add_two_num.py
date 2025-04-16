def main():
    # Get user input
    num1: str = input("Enter your first number: ")
    num1: int = int(num1)
    num2: str = input("Enter your second number: ")
    num2: int = int(num2)
    total: int = num1 + num2
    # Print the result
    print(f"The sum of {num1} and {num2} is {total}.")
    
if __name__ == "__main__":
    main()
    