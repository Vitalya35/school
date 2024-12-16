import random
from random import choice, sample
import string


# def generate_string(length):
#     result = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
#     return result

# print(generate_string(5))

# def generate_string():
#     result = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
#     return result
# def imena(r):
#     e = 0
#     while e < r:
#         print(generate_string())
#         e += 1
#
# imena(2)


                # создание списка имен
# def imena(r):
#     def generate_string():
#         result = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
#         return result
#     e = []
#     while len(e) < r:
#         e.append(generate_string())
#         if len(e) == r:
#             return e
#
# print(imena(10))


                # задаваемый список имен

def vital(r, d):
    def generate_string():
        result = ''.join(random.choice(string.ascii_lowercase) for _ in range(d))
        return result

    e = 0
    while e < r:
        print(generate_string())
        e += 1


vital(3, 8)