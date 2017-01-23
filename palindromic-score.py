"""
Almost palindrome
The palindromic score of a string is the number of errors (characters which do
not match) when the string is read forwards and backwards. For example, the
palindromic score of 'fox' is 2, because 'fox' and 'xof' differ by two characters.
Write a function to take a string and return its palindromic score.
E.g.
"abcdcaa"	2
"aaabbb"	6
"""
# def get_palindrome(string):
#     return string[::-1]

def almost_palindromes(string):
    edit = 0
    last = len(string)-1
    pal = get_palindrome(string)
    print "str and palindrome:"
    print string
    print pal
    i =0
    while i< len(string):
        if string[i] != string[last-i]:
            edit +=1
        i += 1
    print edit
    return edit

almost_palindromes("fox")
almost_palindromes("abbab")
almost_palindromes("cattac")
almost_palindromes("a")
almost_palindromes("abcdcaa") #2
almost_palindromes("aaabbb") #6
