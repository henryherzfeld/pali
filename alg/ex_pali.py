import random
import numpy
import logging

logger = logging.getLogger(__name__)

def pali(word):

    n = len(word)

    if n == 0:
        return 0
    elif n == 1:
        return word

    i = 0
    v = 1
    i_start = 0
    i_end = 0
    max_end = 0
    max_start = 0

    while i < n:

        if i_start > 0:
            i_start = i - 1

        if i_end < n:
            i_end = i + 1

        while i_start > 0 and i_end < n:
            if word[i_start] == word[i_end]:
                print(i_start)
                i_start = i_start - 1
                i_end = i_end + 1

        i = i + 1



    print (word[i_start:i_end-1])


def is_pali(word, i_start, i_end, n):
    i = i_end

    for letter in word[i_start:i_end]:
        if letter != word[i]:
            return 0
        i = i - 1
    return 1
