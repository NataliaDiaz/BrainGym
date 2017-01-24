
"""
Bracket match
A string of brackets is correctly matched if you can pair every opening bracket
up with a later closing bracket, and vice versa. For example, "(()())" is
correctly matched, and "(()" and ")(" are not.
Implement a function which takes a string of brackets and returns the minimum
number of brackets you'd have to add to the string to make it correctly matched.
For example, "(()" could be correctly matched by adding a single closing bracket
at the end, so you'd return 1. ")(" can be correctly matched by adding an opening
bracket at the start and a closing bracket at the end, so you'd return 2.
If your string is already correctly matched, you can just return 0.
E.g.
"(()())"	0
"((())"	1
"())"	1
"""

def bracket_match(bracket_string):
    while '()' in bracket_string >0:
        bracket_string = bracket_string.replace('()', '')
    if bracket_string=='(' or bracket_string ==')':
        return 1
    elif bracket_string =='':
        return 0
    else:# if bracket_string.startswith(')') or bracket_string.startswith('(('):
        # adding ( at the beginning = cost of adding 1 plus the cost of processing
        # the rest of the expression
        return 1 + bracket_match(bracket_string[1:])

bracket_match("(()())")#	0
bracket_match("((())")#	1
bracket_match("())")#	1
