#!/usr/bin/env python3

import os
import sys
import random
import numpy as np
import networkx as nx
import typing as t

src = open("input.txt", "r").readlines()

example = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".splitlines()

# src = example

src = [r.strip() for r in src if r.strip()]


def load(s) -> np.ndarray:
    return np.stack([np.array(list(l)) for l in s])


def label(x: int, y: int) -> str:
    return f"{x}-{y}"


G = nx.DiGraph()
mountain = load(src)
start = ""
end = ""


def value(p: str) -> int:
    if p == "S":
        return 0

    if p == "E":
        return ord("z") - ord("a")

    return ord(p) - ord("a")


def steps(m: np.ndarray, c: int, x: int, y: int) -> t.List[str]:
    s = []
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < m.shape[1] and 0 <= ny < m.shape[0]:
            sz = value(m[ny][nx]) - c
            if sz <= 1:
                s.append(label(nx, ny))
    return s


for y in range(mountain.shape[0]):
    for x in range(mountain.shape[1]):
        p = mountain[y][x]
        c = value(p)
        nid = label(x, y)

        if p == "S":
            start = nid

        if p == "E":
            end = nid

        G.add_node(nid)

        for step in steps(mountain, c, x, y):
            G.add_edge(nid, step)

part1_len = len(nx.dijkstra_path(G, start, end)) - 1
print("part1", part1_len)

shortest = part1_len

for y in range(mountain.shape[0]):
    for x in range(mountain.shape[1]):
        p = mountain[y][x]
        c = value(p)
        if c == 0:
            try:
                l = len(nx.dijkstra_path(G, label(x, y), end)) - 1
                shortest = min(l, shortest)
            except:  # yolo
                pass

print("part2", shortest)


# import matplotlib.pyplot as plt
#
# nx.draw_shell(G, with_labels=True)
# plt.show()
