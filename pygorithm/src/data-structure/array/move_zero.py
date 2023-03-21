target_list = [8, 0, 3, 0, 12]

def move_zero_to_end(nums):
    """ 
    my answer
    Args:
        nums (array): random numbers

    Returns:
        array: arranged nums
    """
    arrange_nums = []
    target = 0
    for i, n in enumerate(nums):
        print(nums)
        if n != 0:
            continue
        beforeIndex = i
        nextIndex = i + 1
        if (nextIndex + 1 == len(nums)):
            break
        while (True):
            beforeValue = nums[beforeIndex]
            nextValue = nums[nextIndex]
            nums[nextIndex] = beforeValue
            nums[beforeIndex] = nextValue
            print(nums)
            print(nextIndex + 1)
            print(len(nums))
            if (nextIndex + 1 == len(nums)):
                break
            beforeIndex += 1
            nextIndex += 1
    return nums

print(move_zero_to_end(target_list))