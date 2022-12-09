#!/usr/bin/env python3

from typing import List

src = open("input.txt", "r").readlines()

example = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".splitlines()

# src = example

src = [r.strip() for r in src if r.strip()]


def move(start, d: str, s: int) -> List[int]:
    cur = start

    for i in range(s):
        if d == "R":
            cur[0] += 1
        elif d == "L":
            cur[0] -= 1
        elif d == "U":
            cur[1] += 1
        elif d == "D":
            cur[1] -= 1
        yield cur


def dump(d: str, head: List[int], knots: List[List[int]]):
    print(d)
    for y in range(4, -1, -1):
        for x in range(6):
            if head[0] == x and head[1] == y:
                print("H", end="")
            else:
                v = "."
                for i, k in enumerate(knots):
                    if k[0] == x and k[1] == y:
                        v = f"{i + 1}"
                        break
                print(v, end="")
        print()
    print()


def move_knot(k1: List[int], k2: List[int], d: str) -> List[int]:
    x_off = abs(k1[0] - k2[0])
    y_off = abs(k1[1] - k2[1])

    if x_off <= 1 and y_off <= 1:
        return k2

    if x_off == 0:
        if k1[1] > k2[1]:
            k2[1] = k1[1] - 1
        elif k1[1] < k2[1]:
            k2[1] = k1[1] + 1
    elif y_off == 0:
        if k1[0] > k2[0]:
            k2[0] = k1[0] - 1
        elif k1[0] < k2[0]:
            k2[0] = k1[0] + 1
    else:
        diag = x_off + y_off > 2

        for c in (0, 1):
            if k1[c] - k2[c] >= 1:
                if diag:
                    k2[c] += 1
                else:
                    k2[c] = k1[c] - 1
            elif k2[c] - k1[c] >= 1:
                if diag:
                    k2[c] -= 1
                else:
                    k2[c] = k1[c] + 1

    assert abs(k1[0] - k2[0]) <= 1, f"{k1} {k2} {d}"
    assert abs(k1[1] - k2[1]) <= 1, f"{k1} {k2} {d}"

    return k2


def run(count: int) -> int:
    head = [0, 0]
    knots = [[0, 0] for _ in range(count)]

    visits = {tuple(knots[-1])}

    for row in src:
        d, s = row.split(" ")

        for head_step in move(head, d, int(s)):
            for i in range(count):
                knots[i] = move_knot(head_step if i == 0 else knots[i - 1], knots[i], d)

            visits.add(tuple(knots[-1]))

        head = head_step

    return len(visits)


print("part1", run(1))
print("part2", run(9))
