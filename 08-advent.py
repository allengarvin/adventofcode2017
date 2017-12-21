#!/usr/bin/python

import os, sys, itertools, string, operator
from parse import parse

def main():
    ops = []

    registers = dict()

    for l in open("../advent/08-input.txt"):
        l = l.strip()
        ops.append(parse("{} {} {} if {} {} {}", l))

    highest = -1

    for var, mod, n, var2, op, val in ops:
        if var not in registers:
            registers[var] = 0
        if var2 not in registers:
            registers[var2] = 0
        if op == "==":
            opf = operator.eq
        elif op == "<=":
            opf = operator.le
        elif op == ">=":
            opf = operator.ge
        elif op == "<":
            opf = operator.lt
        elif op == ">":
            opf = operator.gt
        elif op == "!=":
            opf = operator.ne
        else:
            print "Unknown op ", op

        if opf(registers[var2], int(val)):
            if mod == "inc":
                registers[var] += int(n)
            else:
                registers[var] -= int(n)
        high = sorted(registers.values())[-1]
        if high > highest:
            highest = high

    print "Answer 1: ", sorted(registers.values())[-1]
    print "Answer 2: ", highest
        
    return 1

if __name__ == "__main__":
    main()
