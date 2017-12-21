#!/usr/bin/python

from itertools import combinations

def divisible(arr):
    for c in combinations(arr, 2):
        x, y = sorted(c)
        if y % x == 0:
            return y / x
    print("BUG")
    
def main():
    lines = [map(int, l.strip().split()) for l in open("../advent/02-input.txt").readlines()]
    print "Answer 1:", sum(map(lambda l: max(l) - min(l), lines))
    print "Answer 2:", sum(map(divisible, lines))

if __name__ == "__main__":
    main()
