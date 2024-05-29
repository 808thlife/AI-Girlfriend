import random 
import string 

def get_random_string(length = random.randint(2,10))->str:
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str