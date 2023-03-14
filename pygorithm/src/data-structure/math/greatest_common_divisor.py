def gcf(v1, v2):
    if v1 < 0 or v2 < 0:
        raise ValueError('cannot input negative number')
    gcf_value = None
    if v1 > v2:
        smaller = v2
    else:
        smaller = v1
    for divisor in range(1, smaller + 1):
        if(v1 % divisor == 0) and (v2 % divisor == 0):
            gcf_value = divisor
    return gcf_value

print(gcf(-81, 36))
print(gcf(81, 36))