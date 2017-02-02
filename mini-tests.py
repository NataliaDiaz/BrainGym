# EXERCISE 1
# -- For all integers "i" from 1 to 100, print "Foo" whenever "i" is a multiple
# of 3, print "Bar" whenever "i" is a multiple of 5 and print "FooBar" whenever
# "i" is a multiple of both.

def printing():
    for i in range(1,101):
        if i%3 ==0 and i%5 ==0:
            print i, "FooBar"
        elif i%3 ==0:
            print i, "Foo"
        elif i%5 ==0:
            print i, "Bar"

printing()


# EXERCISE 2
#  -- You have 2 SQL databases:

# "metadata" with column names "path_to_file", "bmi" and "file_id"
# "labels" with column names "file_id", "label_value"

# write a query that will produce a database with 2 columns in it:
# "path_to_file" and "label_value". We only want files for which the
# BMI is found between 10 and 30 (including these end values).

"""

SELECT DISTINCT m.path_to_file, l.label_value
FROM metadata m
JOIN labels l
    ON l.file_id = m.file_id
WHERE m.bmi >= 10 and m.bmi <= 30
ORDER BY m.bmi

"""




############
#EXERCISE 3:
# -- Write a simple function that returns a tuple (x, y) where the point
# (x, y) is uniformly distributed within the unit (so x**2 + y**2 <= 1)

import random

def getTuple():
    """
    returns "x" between [0, 1] uniformly
    """
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    while x**2 + y**2 > 1:
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

    return (x, y)

print getTuple()
print getTuple()
