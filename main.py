#!/usr/bin/env python

import string
from multiprocessing import Pool

index = {}
pool = Pool()


def process_text(text):
    def process_word(word):
        digraphs = tuple(word[x:x + 1] for x in range(len(word) - 1))

        for dig in digraphs:
            if dig[0] in string.ascii_lowercase \
                    and dig[1] in string.ascii_lowercase:
                index[dig] = index[dig] + 1 if dig in index else 1

    pool.map(process_word, text.lower().split())


def process_data():
    total = sum(index.values())

    for dig in index:
        index[dig] = index[dig] / total

    return sorted(index.items(), key=lambda o: o[1], reverse=True)
