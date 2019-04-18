import numpy as np

def pali(word):
    n = len(word)
    lens = np.ones((n, n))

    # initialize solution arr with one and two char palis
    for i in range(n):

        if i < n-1:
            lens[i][i+1] = 2
            lens[i-1][i] = 2


    for i in range(n):
        for j in range(n-1):

                # diagonal movement
                if word[i-1] == word[j+1]:
                    lens[i-1, j+1] = lens[i, j] + 2

                # right movement
                if word[i] == word[j+1]:
                    lens[i, j+1] = lens[i, j] + 1

                # up movement
                if word[j] == word[i-1]:
                    lens[i-1, j] = lens[i, j+1] + 1

    start, end = np.unravel_index(np.argmax(lens), lens.shape)

    if start > end:
        t = end
        end = start
        start = t

    print(word[start:end+1])

    print(lens)
    return word[start:end+1]


# pali("bbananabb")
