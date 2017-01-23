
"""
The deletion distance between two strings is the minimum number of characters
that you need to delete in the two strings in order to have the same string.
The deletion distance between "cat" and "at" is 1, because you can just delete
the first character of cat. The deletion distance between "cat" and "bat" is 2,
because you need to delete the first character of both words. Of course, the
deletion distance between two strings can't be greater than the sum of their
lengths, because you can always just delete both of the strings entirely.

Implement an efficient function to find the deletion distance between two strings.
 Note: see Edit distance, a related concept.
 E.g.
 "at", "cat"	1
 "boat", "got"	3
 "thought", "sloughs"	6
"""

def deletion_distance(str1, str2):
    """
    Setting as template/model word the shortest one composed by only the subset which belongs to the intersection
    of both words, add the rest of extra characters to the initialization value of deletions, and slide
    the other word over it while counting how many characters are not equal while updating two indexes,
    one moving over startWord and other over model, the intersection of both words with the shortest.
    At the end, if some words are not processed, it means they are additions and therefore, they add to
    the deletions score, which is to be returned.
    """
    len1 = len(str1)
    len2 = len(str2)
    intersection = set(list(str1)) & set(list(str2))
    if intersection ==0:
        return len1+len2
    else:
        if len1<len2:
            startWord = str2 # cat
            modelWord = str1 # at
        else:
            startWord = str1
            modelWord = str2
        model = ''
        deletions = 0
        for letter in modelWord:
            if letter in intersection:
                model = model +letter
            else:
                deletions +=1
        i = 0 # index for modelWord
        j = 0 # index for startWord
        while j< len(startWord) and i<len(model):
            if startWord[j] != model[i]:
                deletions +=1
            else:
                i +=1
            j +=1
        if j< len(startWord):
            deletions += (len(startWord)-j)
        if i< len(model):
            deletions += (len(model)-i)
    print "Deletion distance: ",deletions
    return deletions

deletion_distance("at", "cat") # 1
deletion_distance("boat", "got") # 3
deletion_distance("thought", "sloughs") # 6



#  TODO: recursive approach
# def deletion_distance_rec(str1, str2):
#     len1 = len(str1)
#     len2 = len(str2)
#     intersection = set(list(str1)) & set(list(str2))
#     if len(intersection) ==0:
#         return len1+len2
#     else:
#         if len1<len2:
#             startWord = str2
#             modelWord = str1
#         else:
#             startWord = str1
#             modelWord = str2
#         model = ''
#         deletions = 0
#         for letter in modelWord:
#             if letter in intersection:
#                 model = model +letter
#             else:
#                 deletions +=1
#
#         if len1 == 0 and len2 ==0:
#             return deletions
#         elif (len1 == 0 and len2 ==1) or (len2 == 1 and len2 ==0):
#             return deletions +1
#         elif len1 == 1 and len2 ==1:
#             if startWord ==modelWord:
#                 return deletions
#             else:
#                 return deletions + 2
#         else:
#             if len1 >0 and len2 ==0:
#                 return deletions +1+ deletion_distance_rec(startWord[1:], '')
#             elif len2 >0 and len1 ==0:
#                 return deletions +1 + deletion_distance_rec('', modelWord[1:])
#             elif startWord[0] == modelWord[0]:
#                 return deletions + deletion_distance_rec(startWord[1:], modelWord[1:])
#             else:
#                 if startWord[0] in intersection:
#                     return deletions +1 + deletion_distance_rec(startWord, modelWord[1:])
#                 elif modelWord[0] in intersection:
#                     return deletions + 1 + deletion_distance_rec(startWord[1:], modelWord)
#                 else:
#                     return deletions + 2 + deletion_distance_rec(startWord[1:], modelWord[1:])
#
# deletion_distance_rec("at", "cat") # 1
# deletion_distance_rec("boat", "got") # 3
# deletion_distance_rec("thought", "sloughs") #6
