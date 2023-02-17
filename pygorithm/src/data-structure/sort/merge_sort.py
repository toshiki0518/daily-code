import random
# O(n)
def merge_sort(list):
    print(list)
    if len(list) > 1:
        mid = len(list) // 2
        # 左半分
        left = list[:mid]
        # 右半分
        right = list[mid:]
        merge_sort(left)
        merge_sort(right)
        left_i = 0
        right_i = 0
        list_i = 0
        print('list')
        print(left, right, list)
        while (
            left_i < len(left) and
            right_i < len(right)
        ):
            print('index')
            print(left_i, right_i, list_i)
            # 右が大きかったら
            if left[left_i] <= right[right_i]:
                # 左のものを移動して
                list[list_i] = left[left_i]
                # 左のリストのインデックスを移動
                left_i += 1
                print('left right')
                print(left, right, list)
            else:
            # 左が大きかったら
                # 右をのものを移動
                list[list_i] = right[right_i]
                # 右のリストのインデックスを移動
                right_i += 1
                print('list right')
                print(left, right, list)
            # 右のリストのインデックスを移動
            list_i += 1

        while left_i < len(left):
            list[list_i] = left[left_i]
            left_i += 1
            list_i + 1
            print('list left')
            print(left, right, list)
        while right_i < len(right):
            list[list_i] = right[right_i]
            right_i += 1
            list_i + 1
            print('list right2')
            print(left, right, list)
    return list
        


list = [6, 3, 9, 2]
list = random.choices(range(0, 100), k=13)

# print(list)
sorted_list = merge_sort(list)
print(sorted_list)