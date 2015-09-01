#!/usr/bin/env python2

import find_primes

if __name__ == '__main__':
    assert find_primes.trial_division(50) == [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    assert find_primes.sieve_of_eratosthenes(50) == [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    print 'All tests passed!'
