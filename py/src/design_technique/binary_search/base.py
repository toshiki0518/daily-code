import bisect

class BaseBinarySearch:
    def __init__(self) -> None:
        pass

class ArrayBinarySearch(BaseBinarySearch):
    def __init__(self, search_value = 9) -> None:
        super().__init__()
        self.search_value = search_value
        self.sorted_array = [3,5,8,10,14,17,21,39]
        print(self.sorted_array)

    def _search(self):
        left = 0
        right = len(self.sorted_array) - 1
        while right >= left:
            mid = left + (right - left) // 2
            value = self.sorted_array[mid]
            # print("before mid:{},left:{},right:{}".format(mid,left, right))
            if value == self.search_value:
                return mid
            elif value > self.search_value:
                right = mid - 1
            else:
                left = mid + 1
            # print("after mid:{},left:{},right:{}".format(mid,left, right))
        return -1

    def bisect(self):
        arr = [1, 2, 4, 4, 4, 6, 8, 10]

        # 4を挿入するべき位置（最も左の位置）を求める
        position = bisect.bisect_left(arr, 4)
        print(position)  # 出力: 2

    def exec(self, search_value=9):
        self.search_value = search_value
        print("answer: {}".format(self._search()))
        

def main():
    abs = ArrayBinarySearch()
    abs.bisect()
    # abs.exec(10)
    # abs.exec(3)
    # abs.exec(39)

    # abs.exec(-100)
    # abs.exec(9)
    # abs.exec(1000)

if __name__ == "__main__":
    main()