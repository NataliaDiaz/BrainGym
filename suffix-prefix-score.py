"""
Return the substring with highest approximate_matching_score using the prefix,
suffix and text as input. If there are more than one with maximum score, return
the lexicographically smallest substring.
"""

def suffix_score(text, suffix):
    """
    Returns a tuple (substring, n) whith n being the highest score such that the LAST n chars of
    substring sub of text are equal to the FIRST n characters of
    sufix and occur in the same exact order.
    E.g. Suffix_score of "nothing" and "ingenuous" is 3 because "ing"
    is common to the end of "nothing" and beginning of "ingenuous"
    """
    if suffix in text:
        return len(suffix)
    else:
        end = len(suffix)-2
        while end >=0:
            if text.endswith(suffix[0:end]):
                return (suffix[0:end], len(suffix[0:end]))
            else:
                end -=1
        return ("", 0)  # (substring, score)

def approximate_matching_score(text, prefix, suffix):
    text_score = 0
    solutions = []
    (substr, p_score) = suffix_score(text, suffix)
    solutions.append((substr, p_score))
    (substr, s_score) = suffix_score(prefix, text) #suffix_score(text, suffix)
    solutions.append((substr, s_score))
    text_score = p_score + s_score
    lexicographically_smaller_substr = min_lexicographic_solution_with_max_score(solutions)
    return (lexicographically_smaller_substr, text_score)

def min_lexicographic_solution_with_max_score(solutions):
    """
    Input: a list of tuples (substring, score)
    Chooses first max score and then if there is a tie,
    the min lexicographic length solution representing such score
    """
    min_length = []
    min_lex_substr = solutions[0][0]
    max_score = max([sol[1] for sol in solutions])
    max_solutions = {}
    for (substr,score) in solutions:
        if score == max_score:
            max_solutions[substr] = score
            min_lex_substr = substr

    for (substr,score) in max_solutions.iteritems():
        if substr < min_lex_substr: # ord(char)< ord(char):
            min_lex_substr = substr
    print "min_lexicographic_solution: ", min_lex_substr
    return min_lex_substr

print suffix_score("nothing", "ingenuous") #3
print suffix_score("bruno", "nothing") # = prefix_score("nothing", "bruno"): 2
print approximate_matching_score("nothing", "bruno", "ingenuous") # score must be: 5

min_lexicographic_solution_with_max_score([('ing', 3), ('no', 2), ('inn', 3)])

# def all_possible_substrings(txt):
#     allsubstr = [txt]
#     for w in txt:
#         allsubstr.append(w)
#     allsubstr = set(allsubstr)
#     for substringlength in range(2, len(txt)):
#         start = 0
#         end = start + substringlength
#         while start+substringlength <= len(txt):
#             allsubstr.add(txt[start:(start+substringlength)])
#             start +=1
#     print allsubstr
#     return allsubstr

# print suffix_score("nothing", "ingenuous") #3
# print suffix_score("bruno", "nothing") # = prefix_score("nothing", "bruno"): 2
# print approximate_matching_score("nothing", "bruno", "ingenuous") # score must be: 5

#all_possible_substrings('bruno')


# not needed with < operator on strings
# def lexicographic_sort(l):
#     # sorted(l, key=str.upper)
#     # But that may not keep 'A' and 'a' in order, so:
#     return sorted(sorted(l), key=str.upper)


# def prefix_score(text, prefix):
#     """
#     NOT NEEDED: Call suffix_score with switched order parameters
#     Returns the highest n such that the FIRST n chars of
#     substring sub of text are equal to the LAST n characters of
#     prefix and occur in the same exact order.
#     E.g. Prefix_score of "nothing" and "bruno" is 2 because both have a substring "no",
#     that is common to the end of "nothing" and beginning of "ingenuous"
#     """
#     text_score = 0
#     return text_score


# def calculateMinLexicoMaxScore( text,  prefix,  suffix):
#     Brute force
#     solutions = {}
#     split_indexes = range(0, len(text)-2)
#     for substr in substrings(text):
#         if substr not in solutions.keys():
#             solutions[substr] = suffix_score(prefix, substr) + suffix_score(substr, suffix)
#     return min_lexicographic_solution(solutions)

# def calculateMinLexicoMaxScore( text,  prefix,  suffix):
#     solutions = approximate_matching_score(text, prefix, suffix)
#     for sol in solutions:
#         solutions.append(sol)
#     print "Candidate solutions: ",solutions
#     return min_lexicographic_solution(solutions)
