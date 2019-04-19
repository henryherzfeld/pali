import logging

logger = logging.getLogger(__name__)

# define global sentinel characters
sen_char = "@"
start_sen = "!"
end_sen = "#"

def pali(word):

    # convert word to sentinel word
    sen_word = convert(word)

    # store expand length for each index of sen_word
    P = [0] * len(sen_word)

    # center of largest palindrome thus far and its right boundary
    center = right = 0

    # largest expand length and that particular index
    max_len = index = 0

    # loop sen_word to update expand length at each index
    for i in range(1, len(sen_word) - 1):

        # assign mirror using relationship of current LPS center
        mirror = 2 * center - i

        # check if new pali lies within the current LPS
        # and assign its expand length if so
        if i < right:
            P[i] = min(right - i, P[mirror])

        # expand on center of new pali and
        # update expand length at index of new pali
        while sen_word[i + P[i] + 1] == sen_word[i - (P[i] + 1)]:
            P[i] += 1

        # if new pali greater than current LPS
        # assign i to index of new pali and update right boundary
        if i + P[i] > right:
            right = i + P[i]
            center = i

        # update current LPS with new pali length
        if P[i] > max_len:
            max_len = P[i]
            index = i

    # acquire LPS characters from sentinel word array using
    # relationship of LPS index and length
    t_arr = sen_word[ index - max_len: index + max_len + 1 ]

    # remove all sentinel characters
    word_arr = [ c for c in t_arr \
                 if c != sen_char \
                 and c != start_sen \
                 and c != end_sen \
                 ]

    # build LPS as string from word array
    word = "".join(word_arr)

    logger.info(word)
    return word

def convert(word):
    # create copy of array with space to add indices for sentinel characters
    t = [0] * (2 * (len(word)) + 3)

    # add sentinel chars at odd indices, real chars at even indices
    for i in range(len(t)):
        if i == 0:
            t[i] = start_sen
        elif i % 2 == 0 and i < len(t) - 1:
            sen_index = (i - 1) // 2
            t[i] = word[sen_index]
        elif i % 2 == 1 and i < len(t) - 1:
            t[i] = sen_char
        else:
            t[i] = end_sen

    return t
