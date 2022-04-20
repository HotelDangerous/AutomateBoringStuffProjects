# madLibs.py - Takes a madlibs from a .txt file and asks the user to
#              fill in each NOUN, VERB, and ADJECTIVE and then rewrites
#              the file with the users choices.
# Usage: Make sure the file path corresponds to the path on your computer.

import re
import pyinputplus as pyip
from pathlib import Path

path = Path.home() / 'Documents' / 'madLibs.txt'  # Change this to the filepath on your cpu.

# Open and save the contents of a file to a string.
mad_libsFile = open(path)
mad_lib = mad_libsFile.read()
mad_libsFile.close()  # Close the file

# Creating an ordered list of words matching our regular expression.
mad_regex = re.compile(r'ADJECTIVE|NOUN|VERB')
regex_list = mad_regex.findall(mad_lib)

# Pass through the list replacing each occurrence of a VERB, NOUN, or ADJECTIVE
# with a word of users choice.
for word in regex_list:
    if word == 'ADJECTIVE':
        user_word = pyip.inputStr(prompt='Enter an Adjective: ')
    elif word == 'NOUN':
        user_word = pyip.inputStr(prompt='Enter a noun: ')
    else:
        user_word = pyip.inputStr(prompt='Enter a verb: ')

    mad_lib = mad_regex.sub(user_word, mad_lib, 1)  # Changes only the first occurrence of the regex for each loop.

# Reopen file in 'write' mode and replace its content with the user created madlib.
mad_libsFile = open(f'{path}', 'w')
mad_libsFile.write(mad_lib)
mad_libsFile.close()  # Close the file
