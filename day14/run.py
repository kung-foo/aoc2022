#!/usr/bin/env python3

import os
import sys
import random
import numpy as np
from more_itertools import windowed

src = open("input.txt", "r").readlines()

example = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9

""".splitlines()

# src = example

src = [r.strip() for r in src if r.strip()]


def load_cave(infinite_floor: bool) -> (np.ndarray, int):
    mx, my = 0, 0
    minx = 1000
    cave = np.full((1000, 1000), " ")

    def parse_line(line):
        nonlocal mx, my, minx
        for seg_from, seg_to in windowed(line.split(" -> "), 2):
            fx, fy = map(int, seg_from.split(","))
            tx, ty = map(int, seg_to.split(","))

            mx = max(mx, fx, tx)
            my = max(my, fy, ty)
            minx = min(minx, fx, tx)

            if fx > tx:
                fx, tx = tx, fx

            if fy > ty:
                fy, ty = ty, fy

            cave[fy : (ty + 1), fx : (tx + 1)] = "🪨"

    for line in src:
        parse_line(line)

    if infinite_floor:
        parse_line(f"{minx - my},{my + 2} -> {mx + my},{my + 2}")

    cave = cave[0 : my + 1, minx : mx + 1]

    return cave, 500 - minx


def dump(cave):
    with open("cave.txt", "w") as out:
        for y in range(cave.shape[0]):
            for x in range(cave.shape[1]):
                out.write(cave[y][x])
            out.write("\n")


def run(infinite_floor):
    cave, start = load_cave(infinite_floor)

    def val(pos, x_off: int = 0, y_off: int = 0):
        return cave[pos[1] + y_off][pos[0] + x_off]

    def set(pos, char):
        cave[pos[1]][pos[0]] = char

    def move_down(pos) -> bool:
        if val(pos, y_off=1) == " ":
            pos[1] += 1
            return True
        return False

    def move_left(pos) -> bool:
        if val(pos, x_off=-1, y_off=1) == " ":
            pos[0] -= 1
            pos[1] += 1
            return True
        return False

    def move_right(pos) -> bool:
        if val(pos, x_off=1, y_off=1) == " ":
            pos[0] += 1
            pos[1] += 1
            return True
        return False

    c = 0
    abyss = False

    while not abyss:
        sand = [start, 0]

        while True:
            if sand[1] + 1 > cave.shape[0] - 1:
                abyss = True
                break

            if move_down(sand) or move_left(sand) or move_right(sand):
                continue

            set(sand, "💎")
            c += 1

            if sand == [start, 0]:
                dump(cave)
                return c

            break

    return c


print("part1", run(False))
print("part2", run(True))
