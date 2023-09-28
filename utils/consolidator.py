import os
from itertools import chain

# I've gotten some example text files from Project Gutenberg,
# this just gets rid of the formatting and forces lines to a set length.
# This was used to format 3.txt.
# 2.txt was not formatted, intentionally.


def consolidate_text(filename: str, words_per_line: int = 10):
    # Construct the full path to the file
    file_path = os.path.join(os.path.dirname(__file__), '..', 'src', filename)

    # Read the sentences from the file
    with open(file_path, 'r') as f:
        sentences = [line.strip().split() for line in f.readlines()]

    # Flatten the list of words
    words = list(chain.from_iterable(sentences))

    # Reconstruct the text with the specified number of words per line
    consolidated_lines = []
    print(f"Consolidating text with {words_per_line} words per line...")
    for i in range(0, len(words), words_per_line):
        line = ' '.join(words[i:i+words_per_line])
        consolidated_lines.append(line)

    # Write the consolidated text back to the file
    print(f"Writing consolidated text to {file_path}...")
    with open(file_path, 'w') as f:
        for line in consolidated_lines:
            f.write(line + '\n')
    print(f"Consolidated text written to {file_path}")


# Usage:
filename = '3.txt'  # The file you want to consolidate
words_per_line = 50  # Adjust this value as needed
consolidate_text(filename, words_per_line)
