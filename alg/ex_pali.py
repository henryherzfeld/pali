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
    i_start = 0
    i_end = 0
    max_end = 0
    max_start = 0

    while i <= n:
        i_start = i
        i_end = i

        # # check for even-sized palindrome of size 2
        # if i_start:
        #     if is_pali(word, i_start-1, i_start) and max_end - max_start < 2:
        #         max_end = i_start
        #         max_start = i_start-1

        while i_start-1 >= 0 and i_end+1 < n and is_pali(word, i_start-1, i_end+1):

            i_start = i_start - 1
            i_end = i_end + 1
            if max_end - max_start < i_end - i_start:
                max_end = i_end
                max_start = i_start

        i = i + 1
    print(max_start)
    print(max_end+1)
    print(word[max_start:max_end+1])

def is_pali(word, i_start, i_end):
    i = i_end

    for letter in word[i_start:i_end]:
        if letter != word[i]:
            return 0
        i = i - 1
    return 1

pali("AZXCCXZAKIJUTYRFEDSFVBGHYRGTERFD")
