import sys
import os
import math
import random

import sys

# コマンドライン引数を取得
# # arguments = sys.argv[1:]

# # def test_value():
# #     # 引数がまだ残っている場合
# #     if arguments:
# #         try:
# #             # 次の引数を取得して整数に変換
# #             value = int(arguments.pop(0))
# #             return value
# #         except ValueError:
# #             # 整数に変換できない場合はエラー処理
# #             print("無効な引数です。整数を指定してください。")
# #             return None
# #     else:
# #         # 引数がもう残っていない場合
# #         print("引数が不足しています。")
# #         return None

# # if __name__ == "__main__":
# # get_value 関数を呼び出して次の引数を取得
# value1 = test_value()
# if value1 is not None:
#     print(f"取得した値1: {value1}")

# # 再度 get_value 関数を呼び出して次の引数を取得
# value2 = test_value()
# if value2 is not None:
#     print(f"取得した値2: {value2}")


def cal_dist(x1: float, y1: float, x2: float, y2: float):
    print(x1,y1,x2,y2)
    x = (x1 - x2 )
    y = (y1 - y2 )
    return math.sqrt(x**2 + y**2)
    

def closest_point():
    n = get_value()  # 配列の長さ
    x_list = []  # 空のリストを作成

    # N個の要素を追加
    for i in range(n):
        x_list.append(i)

    y_list = [i for i in range(n)]

    minimun_dist: float = 10000000.0

    for i in range(n):
        for j in range(i + 1, n):
            dist: float = cal_dist(x_list[i], y_list[i], x_list[j], y_list[j])
            if dist <= minimun_dist:
                minimun_dist = dist
                # print(minimun_dist)
    print(minimun_dist)


    

class BruteForce:
    INF = 200000000
    def __init__(self) -> None:
        self.arguments = self.get_arguments()
        print("class:", self.__class__.__name__)
        self.random_integers = []
        self.random_integers = self.get_random_num_list()


    def get_arguments(self):
        print(sys.argv[1:])
        return sys.argv[1:]


    def get_random_num_list(self, size = 5):
        random_integers = [random.randint(1, 10) for _ in range(size)]
        print(random_integers)
        return random_integers

    def get_value(self):
        if len(self.arguments) > 0:
            try:
                param1 = int(self.arguments.pop(0))
                return param1
            except ValueError:
                print('value num error')
                return -1
        else:
            print('value empty error')
            return -1

class LinerSearch(BruteForce):
    """_summary_

    Args:
        BruteForce (_type_): _description_
    """
    def __init__(self) -> None:
        super().__init__()
    
    def search(self):
        found_id = self.found_id()
        if found_id is None:
            return False
        return True

    def found_id(self):
        search_value = self.get_value()
        print(search_value)
        for i in self.random_integers:
            if i == search_value:
                return search_value
        return None

    def get_min_value(self):
        min_value = self.random_integers[0]
        for i in self.random_integers:
            if min_value > i:
                min_value = i
        return min_value

    def search_pair(self):
        list1 = self.random_integers
        list2 = super().get_random_num_list()
        threshold = self.get_value()
        min_value = self.INF
        print("Thershold is %d." % (threshold))
        for i in list1:
            for j in list2:
                target = i + j
                if target < threshold:
                    continue
                if target < min_value:
                    min_value = target
                    print("Min value is %d." % (min_value))
        return min_value

    def subset_sub_problem(self):
        sum_list = []
        target = self.get_value()
        result = 0
        for index, i in enumerate(self.get_random_num_list(self.get_value())):
            print("index: %d" % index)
    
def main():
    ls = LinerSearch()
    # result = ls.search()
    # result = ls.found_id()
    # result = ls.get_min_value()
    # result = ls.search_pair()
    # result = ls.get_value()
    # result = ls.get_value()
    result = ls.subset_sub_problem()
    # print(result)



if __name__ == "__main__":
    # 自身のファイル名を取得し、表示する
    script_name = os.path.basename(__file__)
    print(script_name)
    main()

