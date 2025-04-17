def get_first_ele(lst):
    print(lst)
    
def get_lst():
    lst = []
    elem: str = input("Please enter a an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter a an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    get_first_ele(lst)
    
if __name__ == "__main__":
    main()