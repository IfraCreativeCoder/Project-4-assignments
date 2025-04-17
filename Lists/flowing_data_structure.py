def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)
        
        
def main():
    msg = input('Enter a message to copy: ')
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, msg)
    print("List after: ", my_list)
    
if __name__ == "__main__":
    main()