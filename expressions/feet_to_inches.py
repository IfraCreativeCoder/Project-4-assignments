INCHES_IN_FOOT = 12

def main():
    feet: float = float(input("Enter the number of feet: "))
    inches: float = feet * INCHES_IN_FOOT
    print("This is", inches, "inches!")
    
if __name__ == "__main__":
    main()
    
