# This is Python 2
import sys


"""
order-preserving-calculator
Given an expression of 0-9 integers with one + sign and one * sign,
build a method that evaluates the input line from console and returns the
result from the calculator respecting the normal multiplication and addition
preference in the expression order to produce a correct result
TODO: generalize for more than one multiplication and sum
"""
def calculator(line):
    # line = sys.stdin.readline('Input expression contaning a multiplication and addition in any order')
    # line = line.strip()
    print "calculator executing for expression: ",line
    if not line.startswith('+') and not line.startswith('*'):
        if line.find('+') < line.find('*'):
            print " sum comes first in expression..."
            summand, multiplication = line.split('+')
            factor1, factor2 = multiplication.split('*')
        else:
            print " mult comes first in expression..."
            factor1, addition = line.split('*')
            factor2, summand = addition.split('+')

        # do multiplication first no matter what
        result = (int(factor1) * int(factor2))+ int(summand)
        #print factor1,factor2, summand
        print result
        return result
    else:
        print "wrong input format!"

#calculator()
calculator("20+2*3")
calculator("20*2+3")
