def is_palindrome(s):
    str = s.lower()
    return str == str[::-1]

# val = 'blackswan'
val = 'tooomamooot'

print(val)
print(val[::-1])
print(is_palindrome(val))