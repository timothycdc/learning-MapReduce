# This was for formatting 1.txt, taken from the Lorem Ipsum texts.

# read entire text file
# split file into sentences
# rewrite file with 1 sentence per line

import os


def sentence_splitter(filename : str ):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'src', filename)

    with open(file_path, 'r') as f:
        text = f.read()
        sentences = text.split('.')

    with open(file_path, 'w') as f:
        for sentence in sentences:
            f.write(sentence.strip() + '\n')

# Usage 
filename = '1.txt' # change this to the file you want to split
sentence_splitter(filename)
    