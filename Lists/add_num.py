def add_num(numbers)-> int:
    
    total: int = 0
    for number in numbers:
        total += number
    return total

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]
    sum: int = add_num(numbers)
    print(sum)
    
if __name__ == "__main__":
    main()