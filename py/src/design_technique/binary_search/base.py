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

    def exec(self, search_value=9):
        self.search_value = search_value
        print("answer: {}".format(self._search()))
        

def main():
    abs = ArrayBinarySearch()
    abs.exec()
    abs.exec(5)
    abs.exec(39)
    abs.exec(8)
    abs.exec(1000)

if __name__ == "__main__":
    main()