import random
# O(n)
def insertion_sort(list):
    for index in range(1, len(list)):
        val = list[index]
        print(list)
        while index > 0 and list[index - 1] > val:
            print(val)
            list[index] = list[index - 1]
            index = index - 1
        list[index] = val
    return list



list = [6, 5, 8, 2]
list = random.choices(range(0, 100), k=10)

# print(list)
sorted_list = insertion_sort(list)
print(sorted_list)