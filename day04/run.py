#!/usr/bin/env python3

import os
import sys
import random
import numpy as np

src = open("input.txt", "r").readlines()

example = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".splitlines()

# src = example

src = [r.strip() for r in src if r.strip()]


def expand(r):
    l, r = map(int, r.split("-"))
    return np.arange(start=l, stop=r + 1)


p1, p2 = 0, 0

for ass in src:
    a1, a2 = map(expand, ass.split(","))

    if np.isin(a1, a2).all():
        p1 += 1
    elif np.isin(a2, a1).all():
        p1 += 1

    if np.isin(a1, a2).sum() > 0:
        p2 += 1

print("part1", p1)
print("part2", p2)
