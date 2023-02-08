def factorical2(n):
    the_product = 1
    while n > 0:
        the_product *= n
        n = n-1
    return the_product

def factorical(n):
    the_product = 1
    if n == 0:
        return 1
    return n * factorical(n-1)

print(factorical2(5))
print(factorical(5))



