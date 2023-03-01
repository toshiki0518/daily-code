def is_anagram(str1, str2):
    s1 = str1.replace(' ', '').lower()
    s2 = str2.replace(' ', '').lower()
    sort_val1 = sorted(s1)
    sort_val2 = sorted(s2)
    print(sort_val1)
    print(sort_val2)
    return sort_val1 == sort_val2

val1 = 'Emperor Octavian'
val2 = 'Captain over Rome'
print(is_anagram(val1, val2))