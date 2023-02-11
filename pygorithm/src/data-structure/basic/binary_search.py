# O(logn)
def binary_search(values, search):
    start = 0
    end = len(values) - 1
    
    while end >= start :
        mid = (start + end) // 2
        value = values[mid]
        print("mid is %s , search is %s."%(mid, search))
        if(value == search):
            return search
        if search > value :
            start = mid + 1
        else :
            end = mid - 1
    return None


values = list(range(0,300))
search = 39
result = binary_search(values, search)
print('target list is ', values)
print("result is %s ."%result)

