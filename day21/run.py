#!/usr/bin/env python3

import os
import re
import sys
import random
import numpy as np

src = open("input.txt", "r").readlines()

example = """
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
""".splitlines()

# src = example

src = [r.strip().replace(":", " =") for r in src if r.strip()]


def simplify():
    global src

    constants = {}
    src_2 = []

    for r in src:
        ls, rs = r.split(" = ")
        if ls == "humn":
            src_2.append(r)
            continue

        if rs.isnumeric():
            constants[ls] = rs
            continue

        op1, op2 = re.split(r" [\+\-\/\*] ", rs)
        if op1.isnumeric() and op2.isnumeric():
            constants[ls] = str(int(eval(rs)))
            continue

        src_2.append(r)

    src[:] = src_2

    for i, r in enumerate(src):
        ls, rs = r.split(" = ")
        for k, v in constants.items():
            if k in rs:
                rs = rs.replace(k, v)
                src[i] = f"{ls} = {rs}"

    return len(constants) > 0


c = 0
b = len(src)
while simplify():
    c += 1

print(f"removed {b - len(src)} equations using {c} rounds of simplify")

with open("solve.py", "w") as out:
    out.write(
        """#!/usr/bin/env python3
from sympy import solve, symbols, Eq

"""
    )

    symbols = []

    for i, r in enumerate(src):
        symbol = r.split(" = ")[0]
        out.write(f"{symbol} = symbols('{symbol}')\n")
        symbols.append(symbol)

    out.write("\n")

    out.write("f = [\n")

    for i, r in enumerate(src):
        sides = r.split(" = ")
        if sides[0] == "humn":
            continue
        if sides[0] == "root":
            sides[0] = sides[1].split(" + ")[0]
            sides[1] = sides[1].split(" + ")[1]

        out.write(f"    Eq({sides[0]}, {sides[1]}),\n")
    out.write("]\n\n")

    out.write('print("part2", solve(f)[humn])\n')

success = False
passed = set()
root = 0

while not success:
    success = True
    for r in src:
        if r in passed:
            continue
        try:
            exec(r)
            passed.add(r)
        except NameError as ne:
            success = False

print("part1", int(root))
