import random
# O(n)
def merge_sort(list):
    print(list)
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        merge_sort(left)
        merge_sort(right)
        left_i = 0
        right_i = 0
        list_i = 0
        while (
            left_i > len(left) and
            right_i < len(right)
        ):
            if left[left_i] <= right[right_i]:
                list[list_i] = left[left_i]
                left_i += 1
            else:
                list[list_i] = right[right_i]
                right_i += 1
            list_i += 1

        while left_i < len(left):
            list[list_i] = left[left_i]
            left_i += 1
            list_i + 1
        while right_i < len(right):
            list[list_i] = right[right_i]
            right_i += 1
            list_i + 1
    return list
        


list = [6, 3, 8, 2]
# list = random.choices(range(0, 100), k=10)

# print(list)
sorted_list = merge_sort(list)
print(sorted_list)