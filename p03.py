"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def primes(limit):
    MAX = limit
    candidates = [True] * MAX
    candidates[0] = False
    candidates[1] = False

    primelist = []
    for p,isprime in enumerate(candidates):
        if isprime:
            primelist.append(p)
            for n in range(2*p,MAX,p):
                candidates[n] = False
    return primelist

def main():
    i =  600851475143

    pn = primes(200000)

    factors = []
    while i > 1:
        for p in pn:
            if i % p == 0:
                i = i / p
                factors.append(p)
                break
                
    print factors
    print "hello world"

if __name__ == "__main__":
    main()
