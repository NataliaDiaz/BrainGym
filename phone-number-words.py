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
dictionary = set(dictionary)
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
    words = ['']
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
    words = set(words) #valid_words  = [w for w in (dictionary & words)]
    return (dictionary & words) # sets intersection

print decode('4653')
