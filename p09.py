"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math
import itertools

def combinations(l, s):
    c = itertools.combinations(l, 2)
    return [i for i in c if sum(i) == s]


def main():
    
    #sq = [(a, b, c) for a in range(200, 701) for b in range(a, 701) for c in range(b, 701) if a*a + b*b == c*c]

    sq = sorted([n*n for n in range(200, 701)], reverse = True)
    
    for i, s in enumerate(sq):
        if i < len(sq)-1:
            com = combinations(sq[i:], sq[i])
            if len(com):
                for c in com:
                    if (math.sqrt(c[0]) + math.sqrt(c[1]) + math.sqrt(sq[i])) == 1000:
                        print "%d + %d = %d" %(c[0], c[1], sq[i])
                        print math.sqrt(c[0]) * math.sqrt(c[1]) * math.sqrt(sq[i])
                        break


if __name__ == "__main__":
    main()
