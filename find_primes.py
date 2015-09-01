#!/usr/bin/env python2

def trial_division(limit):
    # For each number under the limit, try dividing it by every number that it 
    # could divide evenly into.  We can tell if one number divides evenly into 
    # another by using the modulo (%) operator, which returns the integer 
    # remainder after dividing two numbers.

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

def sieve_of_eratosthenes(limit):
    # The sieve array contains a boolean value for every number between 2 and 
    # the given limit.  The boolean value indicates whether or not that number 
    # could be a prime.  At the beginning of the algorithm, every number could 
    # be a prime (i.e. the array is True everywhere).  As the algorithm 
    # progresses, more and more numbers will be eliminated.  By the end, only 
    # primes will remain.

    primes = []
    sieve = [True for i in range(limit + 1)]

    for candidate in range(2, limit + 1):
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


