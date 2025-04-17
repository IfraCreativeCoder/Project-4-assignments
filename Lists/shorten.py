MAX_LENGHT : int = 5

def shorten(lst):
    while len(lst) > MAX_LENGHT:
        last_elem = lst.pop()
        print(last_elem)
        
def get_lst():
    lst = []
    elem = input("Please enter a an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter a an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)
    
if __name__ == "__main__":
    main()