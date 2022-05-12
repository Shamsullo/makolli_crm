import random


def generate_password():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    # upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'

    all = lower + numbers
    length = 6
    password = ''.join(random.sample(all, length))
    return password
