#!/usr/bin/env python3

import os
import sys
import random
import numpy as np

src = open("input.txt", "r").readlines()

example = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".splitlines()

# src = example

src = [r.strip() for r in src if r.strip()]

s = 0

for line in src:
    h = int(len(line)/2)
    c1, c2 = set(line[0:h]), set(line[h:])

    i = c1.intersection(c2).pop()

    if i.isupper():
        s += ord(i) - ord("A") + 27
    else:
        s += ord(i) - ord("a") + 1

print("part1", s)

s = 0

for g in range(int(len(src)/3)):
    rows = src[g * 3 : (g + 1) * 3]
    b = set(rows[0]).intersection(rows[1]).intersection(rows[2]).pop()

    if b.isupper():
        s += ord(b) - ord("A") + 27
    else:
        s += ord(b) - ord("a") + 1

print("part2", s)
