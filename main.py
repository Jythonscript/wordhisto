#!/usr/bin/env python3

import re

"""
for each line of input file
    until regex on line matches no word
        get word
        check if current word is in dictionary
        if it is
            increment counter by 1
        else
            create it with a counter of 1
        set line equal to group 2 of regex


print dictionary in readable format
"""

"""
test = "Hello, World!"
wordRegex = re.compile("^([A-Za-z]+)(.*)\w")
word = wordRegex.match(test)

if not word:
    print("no match")

print("word: '" + word.group(1) + "'")
print("excess: '" + word.group(2) + "'")
"""

for line in open("input.txt", "r").readlines():
    print("Full line: '" + line[:line.index("\n")] + "'")
    #get word
    wordRegex = re.compile("([A-Za-z]+)(.*)\w")
    word = wordRegex.match(line)
    #check if there are any words left
    if not word:
        #end of line, go to next line
        continue
    print("word: '" + word.group(1) + "'")
    print("excess: '" + word.group(2) + "'")
    print()
