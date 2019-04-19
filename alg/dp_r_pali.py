def pali(word):
    return pali_helper(word, 0, len(word)-1)

def pali_helper(word, start, end):
    # base case 1: single character string
    if start == end:
        return 1

    # base case 2: two character string
    if word[start] == word[end] and start + 1 == end:
        return 2

    # recursive calls to consider palindrome of size - 2
    if word[start] == word[end]:
        return pali_helper(word, start+1, end-1) + 2

    # recursive calls to consider both palindromes of size - 1
    return max(pali_helper(word, start+1, end),
               pali_helper(word, start, end-1))
