import random
import numpy
import logging
import math

logger = logging.getLogger(__name__)

def pali(word):

    n = len(word)

    if n == 0:
        return 0
    elif n == 1:
        return word

    i = 0
    max_end = 0
    max_start = 0

    for i in range(n):
        # consider an even and odd palindrome
        odd = expand_pali(word, i, i)
        even = expand_pali(word, i, i+1)

        # choose max
        max_len = max(odd, even)

        # setting maximum start and end values for current loop iteration
        if max_end - max_start < max_len:
            max_end = i + (max_len // 2)
            max_start = i - ((max_len - 1) // 2)
    print(word[max_start:max_end+1])
    return word[max_start:max_end+1]

def expand_pali(word, start, end):

    while start >= 0 and end < len(word) and word[start] == word[end]:
        start = start - 1
        end = end + 1

    return end - start - 1
