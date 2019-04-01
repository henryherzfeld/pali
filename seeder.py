import random


def seed(n, n_pali, n_words):

    print(n_pali)

    words = []
    # 10 represents number of words to consider per run
    # i.e. 10 words of size 10 in bf, dp, ex, ma
    # 10 words of size 20 in bf, dp, ex, ma...
    for x in range(n_words):
        word = []
        for letter in range(n):
            word.append(chr(random.randint(65, 90)))
        words.append(word)

    return words

# def create_palindrome(n):
#
#     # if odd make it even
#     if n % 2:
#         n = n - 1
#
#
#     for i in range(n):
#         word
#
#
# def insert_palindrome(n):
