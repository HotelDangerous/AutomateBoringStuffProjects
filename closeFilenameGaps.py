# closeFilenameGaps.py - Finds files with a given prefix, spam1.txt
# or spam002.txt, and fills in any number gaps and removes leading zeros.
# Usage - Change the my_path variable to the folder path you wish to organize.

import os, re, shutil

# Change to the directory we wish to work in.
my_path = 'C://delicious'
file_type = '.txt'
cwDir = os.chdir(my_path)

# Define the prefix and suffix with regular expressions.
filenamePattern = re.compile(r"""^([a-zA-Z]+)   # file must begin with a letter or word.
    (0*)?                                       # followed bvy any number of zeros.
    (([123456789])\d*)                          # followed by a number.
    (\.\w*)                                     # followed by any extension.
    """, re.VERBOSE)

# create a list of the contents of the working directory.
cwDir_list = os.listdir(cwDir)

# Loop through the cwd list searching for filenames matching our regex.
for file in cwDir_list:

    # If current object is not a file move to the next item in list.
    if not os.path.isfile(my_path + '/' + file):
        continue

    # Check if the file matches the regex and if not continue to next item in list.
    mo = filenamePattern.search(file)
    if mo == None:
        continue

    # Break filename into its parts
    prefix = mo.group(1)
    zeros = mo.group(2)
    number = mo.group(3)
    extension = file_type

    curr_num = int(number) - 1  # Getting N-1 to search for a gap in numbering.

    # If file has format prefixN.extension, check if prefixN-1.extension exists and fill in gap.
    while curr_num >= 0:
        if os.path.isfile(my_path + '/' + prefix + str(curr_num) + extension) or curr_num == 0:
            shutil.move(my_path + '/' + prefix + zeros + number + extension,
                        my_path + '/' + prefix + str(curr_num + 1) + extension)
            break
        curr_num = curr_num - 1  # Keep decrementing until we find an existing file.
