import numpy as np
import matplotlib.pyplot as plt
import string

def hash_str(string):
    const = 2
    ascii_nums = []

    for i, s in enumerate(string):
        ascii_nums.append(ord(s)*(const**i))

    return sum(ascii_nums)

print(hash_str("abcde"))
