#!/usr/bin/env python3

from more_itertools import windowed, all_unique

src = open("input.txt", "r").readlines()

example = """
bvwbjplbgvbhsrlpgdmjqwftvncz""".splitlines()

# src = example

line = src[0]

sig_len = 14

for i, k in enumerate(windowed(line, sig_len)):
    if all_unique(k):
        print(i + sig_len)
        break
