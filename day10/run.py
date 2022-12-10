#!/usr/bin/env python3

import os
import sys
import random
import numpy as np

src = open("input.txt", "r").readlines()

example = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
""".splitlines()

# src = example

src = [r.strip() for r in src if r.strip()]

cc = 1
ss = 0
x = 1

screen = np.full((6, 40), " ")


def check():
    global ss
    if cc in (20, 60, 100, 140, 180, 220):
        ss += cc * x

    row = cc // 40
    pos = cc % 40 - 1

    for p in (x - 1, x, x + 1):
        if p == pos:
            screen[row][p] = "#"


for row in src:
    check()

    if row == "noop":
        cc += 1
        continue

    cc += 1

    check()

    x += int(row.replace("addx ", ""))
    cc += 1

print("part1", ss)

for row in screen:
    print("".join(row))
