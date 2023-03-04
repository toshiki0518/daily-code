import string

def ciper(a_string = None, key = None):
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    if a_string is None and key is None:
        print(upper_case)
        print(lower_case)
        return ''
    encrypt = ''
    for c in a_string:
        if c in upper_case:
            print(upper_case.index(c))
            new = (upper_case.index(c) + key ) % 26
            print(new)
            encrypt += upper_case[new]
        if c in lower_case:
            print(lower_case.index(c))
            new = (lower_case.index(c) + key ) % 26
            print(new)
            encrypt += lower_case[new]
        else:
            encrypt += c
    return encrypt


print(ciper())
print(ciper('test', 2))
