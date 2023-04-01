def return_list(list1, list2):
    list3 = [v for v in list1 if v in list2]
    return list3

two_weeks_winner = [20, 11, 31, 40, 50, 99, 44]
most_common_winner = [31, 23, 55, 67, 40]

print(return_list(two_weeks_winner, most_common_winner))