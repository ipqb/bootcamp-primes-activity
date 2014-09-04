#!/usr/bin/env python2

def find_primes(limit):
    primes = []

    for candidate in range(2, limit + 1):
        candidate_ok = True

        for divisor in range(2, candidate):
            if candidate % divisor == 0:
                candidate_ok = False
                break

        if candidate_ok:
            primes.append(candidate)

    return primes

if __name__ == '__main__':
    import sys
    limit = int(sys.argv[1])
    print find_primes(limit)


