import math

def main():
    ab = float(input("Enter the length of side AB:"))
    bc = float(input("Enter the length of side BC:"))
    
    bc = math.sqrt(ab**2 + bc**2)
    
    print(f"The length of the hypotenuse is {bc}")
    
if __name__ == "__main__":
    main()
    
    