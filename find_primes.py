#!/usr/bin/env python2

from math import sqrt

def trial_division(limit):
    primes = []

    for candidate in range(2, limit + 1):
        candidate_ok = True

        for divisor in range(2, int(sqrt(candidate)) + 1):
            if candidate % divisor == 0:
                candidate_ok = False
                break

        if candidate_ok:
            primes.append(candidate)

    return primes

def sieve_of_eratosthenes(limit):
    # Create an array containing a boolean value for every number between 2 and 
    # the given limit.  The boolean value indicates whether or not that number 
    # could be a prime.  At the beginning of the algorithm, every number could 
    # be a prime (i.e. the array is True everywhere).  As the algorithm 
    # progresses, more and more numbers will be eliminated.  By the end, only 
    # primes will remain.

    primes = []
    sieve = [True for i in range(limit + 1)]

    for candidate in range(2, limit + 1)
        if sieve[candidate]:
            primes.append(candidate)

            for not_prime in range(2 * candidate, limit + 1, candidate):
                sieve[not_prime] = False

    return primes

if __name__ == '__main__':
    import sys

    algorithm = sys.argv[1]
    limit = int(sys.argv[2])

    if 'div' in algorithm:
        print trial_division(limit)
    elif 'erat' in algorithm:
        print sieve_of_eratosthenes(limit)
    else:
        print 'Unknown algorithm: {}'.format(algorithm)


