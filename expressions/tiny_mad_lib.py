SENTENCE_START: str = "Once upon a time, in a land far away, there lived a "

def main():
    adj: str = input("Please type ad adjective and press enter. ")
    noun: str = input("Please type ad noun and press enter. ")
    verb: str = input("Please type ad verb and press enter. ")
    
    print(SENTENCE_START + adj + " " + noun + " who loved to " + verb + ".")
    
if __name__ == "__main__":
    main()
    