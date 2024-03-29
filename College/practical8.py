import random
"""
random module: This module in Python provides functions to generate random numbers. 
The random.choice() function is used to randomly select elements from a sequence, in this case, characters from the characters string.
"""
import string
"""
string module: The string module contains a collection of string constants. 
In this case, we use string.ascii_letters for lowercase and uppercase letters, string.digits for numbers, and string.punctuation for symbols.
"""


def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(8))
    return password

"""
generate_password() function: This user-defined function generates a password by randomly selecting characters from the characters string.
It uses random.choice() within a list comprehension to create a password of random length between 12 to 16 characters.
"""

new_password = generate_password()
print(new_password)
