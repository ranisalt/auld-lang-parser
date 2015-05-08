#!/usr/bin/env python

import string
from multiprocessing import Pool

digraph_index = {}
letter_index = {l for l in string.ascii_lowercase}
pool = Pool()


def process_text(text):
    def process_word(word):
        if len(word) > 1:
            digraphs = tuple(word[x:x + 1] for x in range(len(word) - 1))

            for dig in digraphs:
                if dig[0] in string.ascii_lowercase \
                        and dig[1] in string.ascii_lowercase:
                    letter_index[dig[0]] += 1
                    digraph_index[dig] = digraph_index[dig] + 1 if dig in digraph_index else 1

        # Words are guaranteed to be >0 char
        if word[-1] in string.ascii_lowercase:
            letter_index[word[-1]] += 1

    pool.map(process_word, text.lower().split())


def process_data():
    total = sum(digraph_index.values())

    for dig in digraph_index:
        digraph_index[dig] = digraph_index[dig] / total

    return sorted(digraph_index.items(), key=lambda o: o[1], reverse=True)
