"""
Given a phone number return all alphabetic representation of the number for
which the word is in a dictionary (globally available).
Example:
4654329 => HOLIDAY
4653 -> GOLF, GOLD, HOLE
## GIVEN:
 4 -> [G, H, I], 6 -> [M, N, O], 5 -> ...
 2 -> [A, B, C]
etc.
Assume you have the dictionary code, code['2'] = ['A', 'B', 'C']

"""

dictionary = ['ADAM', 'APPLE', 'GILD', 'GOLD', 'GOLF', 'HOLD', 'HOLE']
code = {}
code['0'] = []
code['1'] = []
code['2'] = ['A', 'B', 'C']
code['3'] = ['D', 'E', 'F']
code['4'] = ['G','H','I']
code['5'] = ['J', 'K', 'L']
code['6'] = ['M', 'N', 'O']
code['7'] = ['P', 'Q', 'R', 'S']
code['8'] = ['T', 'U', 'V']
code['9'] = ['W', 'X', 'Y', 'Z']


def decode(number):
    words = []
    first_letters = code[number[0]]
    for l in first_letters:
        words.append(l)

    number = number[1:]
    while len(number)>0:
        digit = number[0]
        letters  = code[digit]
        updated_words = []
        for i in range(len(words)):
            for letter in letters:
                updated_words.append(words[i]+letter)
        words = []
        for w in updated_words:
            words.append(w) #words.extend()
        number = number[1:]
    print words
    valid_words  =[]
    for w in words:
        if w in dictionary:
            valid_words.append(w)
    print "Valid words: ",valid_words #= [w if w in voc]

decode('4653')
