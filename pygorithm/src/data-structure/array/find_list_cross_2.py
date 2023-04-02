
two_weeks_winner = [20, 11, 31, 40, 50, 99, 44]
most_common_winner = [31, 23, 55, 67, 40]

set1 = set(two_weeks_winner)
set2 = set(most_common_winner)
list1 = set1.intersection(set2)
print(list(list1))
