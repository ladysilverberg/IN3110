#!/usr/bin/env python

import sys
import os

def wc(filename):
    num_words = 0
    num_lines = 0
    num_characters = 0

    file = open(filename, "r")
    for line in file:
        num_lines += 1
        words = line.split()
        for word in words:
            num_words += 1
        for charater in line:
            num_characters += 1
    file.close()

    print(num_lines, num_words, num_characters, filename)

# Run Word Count
if (len(sys.argv) > 1):
    for filename in sys.argv[1:]:
        wc(filename)
