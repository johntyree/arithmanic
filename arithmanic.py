#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import os
import math
import json
from operator import add, mul, sub, truediv
from collections import namedtuple

import numpy as np

savefile = os.path.expanduser('~/.mentalmath.dat')

Result = namedtuple('Result', 'ok op left right value'.split())

operators = {'+': add, '-': sub, 'x': mul, '/': truediv}


def load(filename):
    with open(filename, 'r') as f:
        dicts = map(json.loads, f)
        record = list(Result(**d) for d in dicts)
    return record


def save(record, filename):
    with open(filename, 'a') as f:
        for r in record:
            dat = json.dumps(r._asdict())
            f.write('{}\n'.format(dat))


def choose_operands(left_range, right_range, shuffle=False):
    left = np.random.random_integers(*left_range)
    right = np.random.random_integers(*right_range)
    if shuffle and np.random.random() > 0.5:
        left, right = right, left
    return (left, right)


def make_q_and_a(op, left, right, digits=1):
    q = "{:{digits}} {} {:{digits}}".format(left, op, right, digits=digits)
    if op == '/' and right == 0:
        a = float('inf')
    else:
        a = operators[op](left, right)
    return q, a


def read(prompt):
    try:
        return raw_input(prompt)
    except NameError:
        return input(prompt)


def eq(resp, a):
    trunc = lambda n: math.floor(10000.0 * float(n)) / 10000.0
    return trunc(resp) == trunc(a)


def make_challenge(op, range1, range2, shuffle):
    left, right = choose_operands(range1, range2, shuffle=shuffle)
    digits = max(map(len, map(str, range1 + range2)))
    q, a = make_q_and_a(op, left, right, digits=digits)

    def challenge():
        resp = read("{} = ".format(q))
        try:
            ok = eq(resp, a)
        except ValueError:
            ok = False
        return Result(ok=ok, op=op, left=left, right=right, value=a)
    return challenge


def show_stats(record):
    import pprint
    pprint.pprint(record)


def main():
    """Run main."""
    import argparse
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument('--range', '-r', type=int, metavar='INT',
                        default=[0, 12], nargs=2,
                        help='Lowest and highest operand values')
    parser.add_argument('--range2', '-r2', type=int, metavar='INT', nargs=2,
                        help='Lowest and highest other operand values')
    parser.add_argument('--ops', '-o', metavar='OPERATION',
                        help='Arithmetic op (+-x/)')
    parser.add_argument('--shuffle', '-s', action="store_true")
    args = parser.parse_args()

    # db = load()

    if args.ops:
        assert set(args.ops) <= set(operators)
        candidate_ops = list(args.ops)
    else:
        candidate_ops = list(operators.keys())

    try:
        record = []
        range1 = args.range
        range2 = args.range2 if args.range2 else args.range
        while True:
            op = np.random.choice(candidate_ops)
            # weights = db[op]
            challenge = make_challenge(op, range1, range2, args.shuffle)
            tries = 2
            while tries:
                result = challenge()
                if not result.ok:
                    print("!!! NO NO NO NO NO !!!")
                record.append(result)
                tries = 0 if result.ok else tries - 1
            if not result.ok:
                print("    {}".format(result.value))
            # weight(weights, left, right, result.ok)
    except EOFError:
        print()
        show_stats(record)
        save(record, savefile)

    return 0

if __name__ == '__main__':
    main()
