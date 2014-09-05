#!/usr/bin/env python2

if __name__ == '__main__':
    from find_primes import trial_division
    from find_primes import sieve_of_eratosthenes

    assert trial_division(50) == [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    assert sieve_of_eratosthenes(50) == [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    print 'All tests passed!'
