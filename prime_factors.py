#!/usr/bin/env python3
#-------------------------------------------------------------------------------
# Calculate the prime factors of a natural number.
#-------------------------------------------------------------------------------

import sys

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0 and is_prime(divisor):
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

if __name__ == '__main__':
    try:
        number = int(sys.argv[1])
        if number <= 0:
            raise ValueError('Please enter a natural integer greater than 0.')

        factors = prime_factors(number)
        print(f'Prime factors of {number}: {factors}')

    except ValueError as e:
        print(f'Error: {e}')
