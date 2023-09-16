import sys
import os
import math
import random

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
    def __init__(self) -> None:
        print("class:", self.__class__.__name__)
        self.random_integers = []
        self.get_num_list()

    def get_num_list(self):
        random_integers = [random.randint(1, 10) for _ in range(5)]
        print(random_integers)
        self.random_integers = random_integers

    def get_value(self):
        if len(sys.argv) > 1:
            try:
                param1 = int(sys.argv[1])
                return param1
            except ValueError:
                print('value error')
                return 0
        else:
            print('value error')
            return 0

# python3 design_technique/brute_force.py 3
class LinerSearch(BruteForce):
    """_summary_

    Args:
        BruteForce (_type_): _description_
    """
    def __init__(self) -> None:
        super().__init__()
    
    def search(self):
        search_value = self.get_value()
        print(search_value)
        for i in self.random_integers:
            if i == search_value:
                return True
        return False

def main():
    ls = LinerSearch()
    result = ls.search()
    print(result)

if __name__ == "__main__":
    # 自身のファイル名を取得し、表示する
    script_name = os.path.basename(__file__)
    print(script_name)
    main()

