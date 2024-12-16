import random
from random import choice, sample
import string


def generate_string(length):
    all_symbols = string.ascii_uppercase + string.digits
    result = ''.join(random.choice(all_symbols) for _ in range(length))
    return result


print(generate_string(4))