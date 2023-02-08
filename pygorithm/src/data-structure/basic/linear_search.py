def linear_search(list, target):
    for val in list:
        if val == target:
            return True
    return False


# linear search is used for search data which is not sorted
target_list = [10, 30, 40, 50, 200, 100, 42]
print(linear_search(target_list, 43))

print(200 in target_list)

fruits = ['apple', 'orange', 'lemon']
print('lemon' in fruits)