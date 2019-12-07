
#To get the documentation from a library

import math
#help(math)

""" 
When we use the / operator we gonna get a float value
To get an integer value we have to use the // operator
"""
print(10/2)
print(10//2)


# We can use r in strings to print what you write is what you get.
path = r'C:\Users\Merline\Documents\Spells'
print(path)


# Putting all together
from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

print(story_words)
