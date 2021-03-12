# generate random names
import random
import string


def generate_random_name():
    file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16)) + '.txt'
    return file_name
