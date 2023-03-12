# print(bin(16))
# print(bin(4))
# print(bin(5))
# print(1 == 1 and 2 == 2)
# print(1== 1 and 2== 3)
# val1 = bin(2)
# val2 = bin(3)
# print(val1)
# print(val2)
# print(0b10 & 0b11)
# print(2 & 3)
# print(2 | 3)

def is_odd(n):
    return n & 1

print(is_odd(11))

def is_power(n):
    return n & (n - 1) == 0

print(is_power(8))