def euclidean_algorithm(v1, v2):
    # if v1 > v2:
    #     base = v1
    #     divisor = v2
    # else :
    #     base = v2
    #     divisor = v1
    # answer = base % divisor
    # print('b%d, d%d, a%d'%(base, divisor, answer))
    # base = divisor
    # divisor = answer
    # while answer != 0:
    #     answer = base % divisor
    #     print('b%d, d%d, a%d'%(base, divisor, answer))
    #     base = divisor
    #     divisor = answer
    # return divisor
    if v1 > v2 :
        (x, y) = (v1, v2)
    else :
        (x, y) = (v1, v2)
    print('x%d, y%d'%(x, y))
    while y != 0:
        (x, y) = (y, x % y)
        print('x%d, y%d'%(x, y))
    return x
print(euclidean_algorithm(99, 333))