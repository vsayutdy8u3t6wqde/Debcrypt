#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from passlib.hash import bcrypt
from libs import pingo
import os
import sys

text_file = open("pass.txt", "r")
words = text_file.read().splitlines()
hash = '$2y$10$M6suvr2adomojMJjs/OEcu/7XLxp9nkdWgFlemdZ2wq23hIQG6P3.'
length = len(words)

correct_word = ""
for (index, word) in enumerate(words):
    pingo(index, length, prefix='Wait:', suffix='Complete')
    correct = bcrypt.verify(word, hash)
    if (correct):
        correct_word = word
        print()
        break

print("Results:", correct_word)
