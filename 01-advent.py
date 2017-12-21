#!/usr/bin/python

def main():
    input = open("../advent/01-input.txt").readline().strip()
    vals = map(int, list(input))
    print "Answer 1:", sum(map(lambda n: vals[n] if vals[n] == vals[(n+1) % len(vals)] else 0, range(len(vals))))
    print "Answer 2:", sum(map(lambda n: vals[n] if vals[n] == vals[(n+len(vals)/2) % len(vals)] else 0, range(len(vals))))

if __name__ == "__main__":
    main()
