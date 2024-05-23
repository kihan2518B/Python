import string
import random

def genratePassword():
    union = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(union) for i in range(6))
    return password

print(genratePassword())