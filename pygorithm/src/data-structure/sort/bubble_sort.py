def bubble_sort(targets):
    last = len(targets) - 1
    for i in range(last):
        for j in range(last):
            target = targets[j]
            next = targets[j + 1]
            if target > next:
                targets[j] = next
                targets[j + 1] = target
            print(targets)              


def bubble_sort_exclude_sorted(targets):
    last = len(targets) - 1
    for i in range(last):
        no_swaps = True
        for j in range(last):
            target = targets[j]
            next = targets[j + 1]
            if target > next:
                targets[j] = next
                targets[j + 1] = target
                no_swaps = False
            print(targets)
        print(no_swaps)
        if no_swaps:
            return targets
    return targets

targets = [32, 1, 9, 6]
# targets = [1, 6, 9, 32]

print(targets)
# sort_targets = bubble_sort(targets)
sort_targets = bubble_sort_exclude_sorted(targets)
