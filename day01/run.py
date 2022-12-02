#!/usr/bin/env python3

import os
import sys
import random
import numpy as np

src = open("input.txt", "r").readlines()

example = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".splitlines()

# src = example

src = [r.strip() for r in src]

elves = [0]

for i in range(len(src)):
    if not src[i]:
        elves.append(0)
        continue
    elves[-1] += int(src[i])

print("part1", max(elves))
# print(elves.index(max(elves)) + 1)

elves.sort(reverse=True)

print("part2", np.sum(elves[0:3]))
