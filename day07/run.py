#!/usr/bin/env python3

import os
import re
import sys
import random
import numpy as np
from attrs import define
from typing import List, Dict, Any
from icecream import ic

src = open("input.txt", "r").readlines()

example = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".splitlines()

# src = example

src = [r.strip() for r in src if r.strip()]

re_dir = re.compile(r"dir (.+)")
re_file = re.compile(r"(\d+) (.+)")
re_cd = re.compile(r"\$ cd (.+)")


@define
class Entry:
    name: str
    parent: "Entry"
    children: "Dict[str, Entry]" = {}
    files: Dict[str, int] = {}

    def size(self) -> int:
        sz = 0

        for _, v in self.files.items():
            sz += v

        for c in self.children.values():
            sz += c.size()

        return sz


root = Entry(name="/", parent=None, children={}, files={})
current = root

files = set()

for line in src:
    if line == "$ cd /":
        current = root
    elif m := re_dir.match(line):
        d = m.group(1)
        current.children[d] = Entry(name=d, parent=current, children={}, files={})
    elif m := re_file.match(line):
        current.files[m.group(2)] = int(m.group(1))
    elif line == "$ cd ..":
        current = current.parent
    elif m := re_cd.match(line):
        current = current.children[m.group(1)]
    elif line == "$ ls":
        pass  # nop
    else:
        raise Exception(f"not handled: {line}")

sz = 0


def recurse_p1(entry: Entry):
    global sz
    if entry.size() <= 100000:
        sz += entry.size()
    for c in entry.children.values():
        recurse_p1(c)


recurse_p1(root)

print("part1", sz)

dirs = []


def recurse_p2(entry: Entry):
    dirs.append((entry.size(), entry.name))
    for c in entry.children.values():
        recurse_p2(c)


recurse_p2(root)

dirs = sorted(dirs, key=lambda k: k[0])

free = 70_000_000 - root.size()

for i, d in enumerate(dirs):
    if d[0] + free >= 30_000_000:
        print("part2", d)
        break
