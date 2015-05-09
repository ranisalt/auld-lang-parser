#!/usr/bin/env python

import string
import sys

allowed_letters = string.ascii_lowercase
digraph_index = {}
letter_index = {l : 0 for l in allowed_letters}


def process_text(text):
    def process_word(word):
        if len(word) > 1:
            digraphs = tuple(word[x:x + 2] for x in range(len(word) - 1))

            for dig in digraphs:
                if dig[0] in allowed_letters and dig[1] in allowed_letters:
                    letter_index[dig[0]] += 1
                    digraph_index[dig] = digraph_index[dig] + 1 \
                            if dig in digraph_index else 1

        # Words are guaranteed to be >0 char
        if word[-1] in allowed_letters:
            letter_index[word[-1]] += 1

    for word in text.lower().split():
        process_word(word)


def process_data():
    total = sum(digraph_index.values())

    # This calculates the PERCENTAGE over the COUNT
    for dig in digraph_index:
        digraph_index[dig] = digraph_index[dig] / total

    return sorted(digraph_index.items(), key=lambda o: o[1], reverse=True)


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        with open(arg) as raw:
            for line in raw:
                process_text(line)

    print(process_data())
