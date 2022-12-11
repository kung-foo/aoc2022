#!/usr/bin/env python3

import re
import numpy as np
from more_itertools import chunked
from attrs import define
import typing as t

src = open("input.txt", "r").readlines()

example = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".splitlines()

# src = example

src = [r.strip() for r in src if r.strip()]


@define
class Monkey:
    id: int
    items: t.List[int]
    test: int
    on_true: int
    on_false: int
    worry: t.Callable
    inspected: int = 0


def make_monkeys() -> t.List[Monkey]:
    monkeys = []

    for mdef in chunked(src, 6):
        m = Monkey(
            id=int(re.match(r"Monkey (\d+):", mdef[0]).group(1)),
            items=[
                int(x)
                for x in re.match(r"Starting items: (.*)", mdef[1]).group(1).split(", ")
            ],
            test=int(re.match(r"Test: divisible by (\d+)", mdef[3]).group(1)),
            on_true=int(re.match(r"If true: throw to monkey (\d+)", mdef[4]).group(1)),
            on_false=int(
                re.match(r"If false: throw to monkey (\d+)", mdef[5]).group(1)
            ),
            worry=eval(
                "lambda old: " + re.match(r"Operation: new = (.*)", mdef[2]).group(1)
            ),  # :-D
        )
        monkeys.append(m)
        assert m.id == len(monkeys) - 1

    return monkeys


def part1():
    monkeys = make_monkeys()

    for i in range(20):
        for m in monkeys:
            m.inspected += len(m.items)
            for item in m.items:
                item = m.worry(item) // 3
                if item % m.test == 0:
                    monkeys[m.on_true].items.append(item)
                else:
                    monkeys[m.on_false].items.append(item)
            m.items.clear()

    busy = sorted(monkeys, key=lambda m: m.inspected, reverse=True)

    print("part1", busy[0].inspected * busy[1].inspected)


def part2():
    monkeys = make_monkeys()

    fix = int(np.product([m.test for m in monkeys]))

    for i in range(10_000):
        for m in monkeys:
            m.inspected += len(m.items)
            for item in m.items:
                item = m.worry(item) % fix

                if item % m.test == 0:
                    monkeys[m.on_true].items.append(item)
                else:
                    monkeys[m.on_false].items.append(item)
            m.items.clear()

    busy = sorted(monkeys, key=lambda m: m.inspected, reverse=True)

    # for m in monkeys:
    #     print(f"Monkey {m.id} inspected items {m.inspected} times.")

    print("part2", busy[0].inspected * busy[1].inspected)


part1()
part2()
