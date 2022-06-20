import random
import string
from time import sleep


def generate():
    """
    This function generates a strong 20-chars password, e.g.
    fcAc8c-1adb0e-CE3e8e
    """
    return '-'.join([
        ''.join(random.choices(string.hexdigits, k=6)) for i in range(3)
        ])


if __name__ == '__main__':
    print(generate())
    sleep(30)
