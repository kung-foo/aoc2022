#!/usr/bin/env python3

import os
import sys
import random
import numpy as np
import re

src = open("input.txt", "r").readlines()

example = """
    [D]
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".splitlines()

# src = example

move_re = re.compile(r"move (\d+) from (\d+) to (\d+)")


def parse():
    stacks = {}
    moves = []

    for i, line in enumerate(src):
        if not line:
            pass

        if "[" in line:
            line = line + " " * (40 - len(line))
            for c in range(9):
                if (l := line[c * 4 + 1]) and l != " ":
                    c += 1

                    if c not in stacks:
                        stacks[c] = []

                    stacks[c].insert(0, l)
        else:
            if m := move_re.match(line):
                moves.append([int(m.group(1)), int(m.group(2)), int(m.group(3))])

    return stacks, moves


stacks, moves = parse()

for move in moves:
    c, f, t = move

    for i in range(c):
        stacks[t].append(stacks[f].pop())

part1 = ""

for k in sorted(stacks.keys()):
    part1 += stacks[k][-1]

print("part1", part1)

###

stacks, moves = parse()

for c, f, t in moves:
    stacks[t].extend(stacks[f][-c:])
    del stacks[f][-c:]

part2 = ""

for k in sorted(stacks.keys()):
    part2 += stacks[k][-1]

print("part2", part2)
