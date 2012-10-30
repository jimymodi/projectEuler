"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def main():

    MAX = 104750
    l = [True] * MAX
    l[0] = l[1] = False
    primes = []
    for p, isprime in enumerate(l):
        if isprime:
            primes.append(p)
            for n in range(2*p,MAX,p):
                l[n] = False
    print (primes)

if __name__ == '__main__':
    main()
