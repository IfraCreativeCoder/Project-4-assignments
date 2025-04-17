def get_last_elem(lst):
    print(lst(-1))
    
def main():
    user_input = input("Please enter a list of elements separated by comma: ")
    my_list = user_input.split(",")

    get_last_elem(my_list)

if __name__ == "__main__":
    main()
