import random
import string

def gene_passw(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

passw_length = 8
generated_passw = gene_passw(passw_length)
print("Generated Password:", generated_passw)
