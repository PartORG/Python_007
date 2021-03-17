# generate random names
import random
import string


def generate_random_name():
    """
    This function generates a random name for a txt-file.
    Name is generated only with letters.
    Length of generated file name is 16 characters.

    Input: - None -
    Output: Generated text file name with extension (.txt).
    """

    file_name = f"{''.join(random.choice(string.ascii_lowercase) for _ in range(16))}.txt"
    return file_name
