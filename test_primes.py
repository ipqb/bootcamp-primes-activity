#!/usr/bin/env python2

if __name__ == '__main__':
    from find_primes import find_primes

    assert find_primes(50) == [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    print 'All tests passed!'
