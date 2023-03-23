a_set = set()
a_set.add('justin bieber')
a_set.add('kendall jenner')
a_set.add('kanye west')
a_set.add('justin bieber')
# print(a_set)


def dups(list):
    dups = []
    check = set()
    for item in list:
        l1 = len(check)
        check.add(item)
        l2 = len(check)
        if l1 == l2:
            dups.append(item)
    return dups

a_list = ['tanaka',
          'suzuki',
          'tanaka',
          'lemon',
          'dog']

print(dups(a_list))