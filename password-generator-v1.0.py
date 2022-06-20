import random
import string
from time import sleep


def generate():
    """
    This function generates a strong 20-chars password, e.g.
    Qwert1-Yuiop2-Asdfg3
    """
    return '-'.join([
        ''.join((
            ''.join(map(str, random.choices(string.ascii_lowercase, k=5))),
            random.choice(string.digits))).capitalize() for i in range(3)])


if __name__ == '__main__':
    print(generate())
    sleep(30)
