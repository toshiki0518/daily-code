import sys
import math
import random
from itertools import combinations


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
    def __init__(self, is_unique = False, list_length = 5) -> None:
        print("class:", self.__class__.__name__)
        self.random_integers = []
        self.random_integers = self.get_random_num_list(is_unique, list_length)
        self.pointer = 0

    def get_random_num_list(self, is_unique = False, list_length = 5):
        if is_unique is True:
            # 重複のないランダムな整数のリストを生成
            unique_numbers = random.sample(range(1, 10), list_length)
            # print(unique_numbers)
            return unique_numbers
        # 重複あり
        random_integers = [random.randint(1, 10) for _ in range(list_length)]
        # print(random_integers)
        return random_integers

    def get_value(self):
        """
        get parameter value
        if parameter value does not exist
        input some value and convert int 

        Returns:
            _type_: _description_
        """
        if len(sys.argv) > 1:
            try:
                self.pointer += 1
                param1 = int(sys.argv[self.pointer])
                return param1
            except ValueError:
                print('value error')
                return 0
        else:
            # Prompt the user for input
            param1 = input("Please enter something: ")

            # Display the user's input
            print("Entered value:", param1)
            param1 = param1 if param1 else "0"
            return int(param1)

