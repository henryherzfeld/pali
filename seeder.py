import random
import numpy as np


def seed(n, n_pali, n_words):

    words = []

    for x in range(n_words):
        word = []
        for letter in range(n):
            word.append(chr(random.randint(65, 90)))

        word = insert_pali(word, n_pali)

        words.append(word)

    return words

# inserts a palindrome into a given char array at a random index
def insert_pali(word, n):
        i_start = random.randint(0, (len(word) - n - 1))

        pali = get_pali(n)

        for i, letter in enumerate(pali):
            word[i_start + i] = letter

        return word


def get_pali(n):

    if n % 2:
        n = n - 1

    word = np.empty(n, dtype=object)

    for i in range(n//2):
        rand = chr(random.randint(65, 90))
        word[i] = rand
        word[n-i-1] = rand

    return word
