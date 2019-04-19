import logging

logger = logging.getLogger(__name__)

def pali(word):

    # initialization
    n = len(word)
    i_start = 0
    i_end = 0
    max_end = 0
    max_start = 0

    # handle small input strings
    if n == 0:
        return 0
    if n == 1:
        return word

    # move start index through entire word
    while i_start <= n:
        i_end = i_start + 1

        # move end index through entire word
        while i_end < n:

            # test current substring
            if is_pali(word, i_start, i_end):

                # if palindrome size is greater than max palindrome
                # assign palindrome size to max palindrome
                if i_end - i_start >= max_end - max_start:
                    max_start, max_end = i_start, i_end

        # loop iterators
            i_end = i_end + 1
        i_start = i_start + 1

    logger.info(word[max_start:max_end+1])
    return word[max_start:max_end+1]

# employs "onion" or peel method to test palindrome within
# given start and end indices
def is_pali(word, i_start, i_end):
    i = i_end

    for letter in word[i_start:i_end]:
        if letter != word[i]:
            return 0
        i = i - 1
    return 1
