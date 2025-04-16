def fah_to_cel():
    """Convert Fahrenheit to Celsius."""
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
    
if __name__ == "__main__":
    fah_to_cel()
    
    