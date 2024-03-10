import random
import requests 
import string 

def pass_gen(num: int = 12):
    """
    This function generates a random password by combining uppercase letters, lowercase letters, punctuation marks, and digits.

    Parameters:
    - num (int): The length of the generated password. Default is 12 if not specified.

    Returns:
    - str: A randomly generated password consisting of characters from string.ascii_letters, string.punctuation, and string.digits.

    Example usage:
    >>> pass_gen()
    'r$6Ag~P{32F+'
    >>> pass_gen(10)
    'ZnK"9|?v3a'
    """
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.sample(characters, num))
    return password
