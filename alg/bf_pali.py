import logging

logger = logging.getLogger(__name__)

def pali(word):

    n = len(word)
    if n == 0:
        return 0

    elif n == 1:
        return word

    i_start = 0
    i_end = 0
    max_end = 0
    max_start = 0


    while i_start <= n:
        i_end = i_start + 1
        while i_end < n:
            if is_pali(word, i_start, i_end):
                if i_end - i_start >= max_end - max_start:
                    max_start, max_end = i_start, i_end
            i_end = i_end + 1
        i_start = i_start + 1

    logger.info(word[max_start:max_end+1])
    return word[max_start:max_end+1]

def is_pali(word, i_start, i_end):
    i = i_end

    for letter in word[i_start:i_end]:
        if letter != word[i]:
            return 0
        i = i - 1
    return 1
