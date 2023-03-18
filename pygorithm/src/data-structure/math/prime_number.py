# 素数
def is_prime(n):
    for i in range(2, n):
        print(i)
        if n % i == 0:
            return False
    return True

# print(is_prime(11))
# print(is_prime(2))
# print(is_prime(9))

import math

def is_prime_improvment(n):
    # print(n)
    square_root_of_n = int(math.sqrt(n))
    # print(square_root_of_n)
    square_root_of_n = square_root_of_n + 1
    # print(square_root_of_n)
    for i in range(2, square_root_of_n):
        # print(i)
        if n % i == 0:
            return False
    return True

# print(is_prime_improvment(11))
# print(is_prime_improvment(2))
# print(is_prime_improvment(9))
# print(is_prime_improvment(169))

def find_primes(n):
    return [i for i in range(2, n) if is_prime_improvment(i)]

print(find_primes(100))
