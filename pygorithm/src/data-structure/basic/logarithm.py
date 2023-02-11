def log2(n):
    result = 0
    while n >= 2:
        n = n / 2
        result += 1
    return result

print(log2(8)) # Output: 3

def calc_log(n):
    result = 0
    temp = 1
    while temp <= n:
        temp = temp * 2
        result += 1
    return result

values = list(range(0,100))
for value in values :
    print('value is %s, result is %s'%(value, calc_log(value)))