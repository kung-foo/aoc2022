#!/usr/bin/env python3
import json
import os
import sys
import random
from enum import Enum
from more_itertools import chunked, windowed
import typing as t
from functools import cmp_to_key

yolo = eval

src = open("input.txt", "r").readlines()

example = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".splitlines()

# src = example
src = [yolo(r.strip()) for r in src if r.strip()]


class Action(Enum):
    Yep = 1
    Nope = 2
    HellIfIKnow = 3


def check_list(l: t.List[t.Any], r: t.List[t.Any]) -> Action:
    for p1, p2 in zip(l, r):
        if (ret := check(p1, p2)) != Action.HellIfIKnow:
            return ret

    if len(l) == len(r):
        return Action.HellIfIKnow

    if len(l) < len(r):
        return Action.Yep
    else:
        return Action.Nope


def check(l, r) -> Action:
    if isinstance(l, list) and isinstance(r, list):
        return check_list(l, r)

    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return Action.Yep
        if l > r:
            return Action.Nope
        return Action.HellIfIKnow

    if isinstance(r, int):
        return check(l, [r])

    if isinstance(l, int):
        return check([l], r)

    assert False, "wtf"


def part1():
    is_true = []

    for i, (l, r) in enumerate(chunked(src, 2)):
        if check(l, r) == Action.Yep:
            is_true.append(i + 1)

    print("part1", sum(is_true))


def flatten(row, depth: int = 1) -> str:
    if len(row) == 0:
        return depth * "0"

    s = ""
    for x in row:
        if isinstance(x, int):
            s += str(x)
        else:
            s += flatten(x, depth + 1)

    return s


def cmp(l: t.List[t.Any], r: t.List[t.Any]) -> int:
    c = check(l, r)
    if c == Action.Nope:
        return 1
    if c == Action.Yep:
        return -1
    assert False, "crap"


def part2():
    src.append([[2]])
    src.append([[6]])

    list.sort(src, key=cmp_to_key(cmp))

    # for i, (l, r) in enumerate(windowed(src, 2)):
    #     assert check(l, r) == Action.Yep

    print("part2", (src.index([[2]]) + 1) * (src.index([[6]]) + 1))


part1()
part2()
