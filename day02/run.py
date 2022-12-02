#!/usr/bin/env python3

import os
import sys
import random
import numpy as np

src = open("input.txt", "r").readlines()

example = """
A Y
B X
C Z
""".splitlines()

# src = example

src = [r.strip() for r in src if r.strip()]

outcomes = {
    "A X": 1 + 3,
    "A Y": 2 + 6, # 4
    "A Z": 3 + 0,
    "B X": 1 + 0, # 1
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3, # 7
}

score = 0

for g in src:
    score += outcomes[g]

print("part1", score)

outcomes = {
    "A X": 0 + 3,
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 0 + 2,
    "C Y": 3 + 3,
    "C Z": 6 + 1,
}

score = 0

for g in src:
    score += outcomes[g]

print("part2", score)