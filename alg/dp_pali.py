import numpy as np
import logging

logger = logging.getLogger(__name__)

def pali(word):

    # initialization
    n = len(word)
    lens = np.ones((n, n))

    for i in range(n):

        # update matrix to reflect odd palindromes centered on sentinel
        if i < n-1:
            lens[i][i+1] = 2
            lens[i-1][i] = 2

    # move through matrix row by row
    # i is start, j is end of considered pali
    for i in range(n):
        for j in range(n-1):

                # each movement corresponds to an increase in considered
                # diagonal movement
                if word[i-1] == word[j+1]:
                    lens[i-1, j+1] = lens[i, j] + 2

                # right movement
                if word[i] == word[j+1]:
                    lens[i, j+1] = lens[i, j] + 1

                # up movement
                if word[j] == word[i-1]:
                    lens[i-1, j] = lens[i, j+1] + 1

    # use maximum pali length in lens array to
    # return indices of longest palindrome
    start, end = np.unravel_index(np.argmax(lens), lens.shape)

    # ensure movement in matrix did not reverse start, end
    if start > end:
        t = end
        end = start
        start = t

    logger.info(word[start:end+1])

    return word[start:end+1]
