"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def isdivisible(n):
    f = True
    for i in range(11,21):
        if n % i != 0:
            f = False
            break
    return f

def main():
    
    for n in range(2520,500000000,2520):
        if isdivisible(n) :
            print n, "is ans"
            break

if __name__ == '__main__':
    main()
