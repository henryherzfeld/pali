def pali_helper(word, max_start, max_end, i_start, i_end):
    n = len(word)

    if n == 0:
        return 0

    if n == 1:
        return 0

    if i_start == n-2:
        if max_end:
            print(word[max_start:max_end+1])
            return word[max_start:max_end]

    if i_end >= n:
        i_start = i_start + 1
        i_end = i_start + 1

    if is_pali(word, i_start, i_end):
        if i_end - i_start >= max_end - max_start:
            max_start, max_end = i_start, i_end

    pali_helper(word, max_start, max_end, i_start, i_end+1)

def pali(word):
    pali_helper(word, 0, 0, 0, 1)

def is_pali(word, i_start, i_end):
    i = i_end
    print(i_end)

    for letter in word[i_start:i_end]:
        if letter != word[i]:
            return 0
        i = i - 1
    return 1
