'''http://www.ardendertat.com/2011/10/10/programming-interview-questions-6-combine-two-strings/
Combine two strings
We are given 3 strings: str1, str2, and str3. Str3 is said to be a shuffle of str1 and str2 if it can be formed by interleaving the characters of str1 and str2 in a way that maintains the left to right ordering of the characters from each string. For example, given str1=”abc” and str2=”def”, str3=”dabecf” is a valid shuffle since it preserves the character ordering of the two strings. So, given these 3 strings write a function that detects whether str3 is a valid shuffle of str1 and str2.


- See more at: http://www.ardendertat.com/2011/10/10/programming-interview-questions-6-combine-two-strings/#sthash.vaaPe4cF.dpuf'''

from queue import Queue

def isShuffle(str1, str2, str3):
    A = Queue() # First in, first out (FIFO queue)
    B = Queue()
    
    for i in range(len(str1)-1, 0):
        A.push(str1[i])
    
    for j in range(len(str2)-1, 0):
        B.push(str1[i])
    
    for c in str3:
        if c in A:
            # non supported operation in Python for queues: we can do:
            # while A.size()>0, A.pop(), but it is too late once popped if
            # the letter is not the one we are processing in word c.
            # We use lists instead and increment indexes accordingly.
            if not c == A.pop():
                if not c == B.pop():
                    return False
        elif c in B:
            if not c == B.pop():
                if not c == A.pop():
                    return False
        else:
            return False
            
            
isShuffle("akdjfk", "ieriqu", "kjdf")
isShuffle("abc", "def","dabecf")
