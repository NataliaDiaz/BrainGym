"""
Longest palindromic substring
A palindrome is a string which reads the same forwards as backwards, for example "abba" or "racecar"
or "bob".
Write a function which returns the length of the longest palindromic substring of a given string.
For example, the longest palindromic substring of "bobcat" is "bob", so you'd return 3.
You do not need to come up with an optimized algorithm for this. A simple search through all substrings is fine.
E.g.
"abba" 4
"bobcat" 3
"acyclic" 3
"""
def is_palindrome(string):
    return string == string[::-1]

def get_palindroms_of_size(string, N):
    start = 0
    palindromes = []
    while (start+N)<= len(string):
        if is_palindrome(string[start:(start+N)]):
            palindromes.append(string[start:(start+N)])
        start +=1
    return palindromes

def longest_palindromic_substring(string):
    longest = 0
    i = 0
    N = len(string)
    while N>0:
        palindromes = get_palindroms_of_size(string, N)
        for palindrome in palindromes:
            if len(palindrome) >longest:
                longest= len(palindrome)
            if longest>0:
                print longest
                return longest
        N -=1
    print longest
    return longest

longest_palindromic_substring("abba")
longest_palindromic_substring("bobcat")
longest_palindromic_substring("acyclic")
