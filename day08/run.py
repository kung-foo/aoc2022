#!/usr/bin/env python3

import os
import sys
import random
import numpy as np

src = open("input.txt", "r").readlines()

example = """
30373
25512
65332
33549
35390
""".splitlines()

# src = example

src = [r.strip() for r in src if r.strip()]

dim = len(src)


def make_forest(s) -> np.ndarray:
    return np.stack([np.array(list(l), dtype=np.int8) for l in s])


f = make_forest(src)


def icu(f: np.ndarray) -> np.ndarray:
    m = np.zeros(f[0].shape, dtype=np.int8)

    def find_max(a: np.ndarray) -> np.ndarray:
        nonlocal m
        p = m
        m = np.maximum(m, a)
        return p + 1

    x = np.apply_along_axis(find_max, 1, f)
    x[0] = 0

    return f >= x


h = np.full(f.shape, fill_value=False)

# tom would put this on one line
h |= icu(f)
h |= np.flip(icu(np.flip(f)))
h |= icu(f.T).T
h |= np.flip(icu(np.flip(f).T)).T

print("part1", h.sum())


def tree_see(f: np.ndarray) -> np.ndarray:
    def how_many(row: np.ndarray) -> np.ndarray:
        viz = np.zeros(row.shape, dtype=np.int8)

        for i, v in enumerate(row):
            pos = i + 1
            while pos < dim:
                viz[i] += 1
                if row[pos] >= v:
                    break
                pos += 1
        return viz

    return np.apply_along_axis(how_many, 1, f)


h = np.ones(f.shape, dtype=np.int32)

h *= tree_see(f)
h *= np.flip(tree_see(np.flip(f)))
h *= tree_see(f.T).T
h *= np.flip(tree_see(np.flip(f).T)).T

print("part2", h.max())
