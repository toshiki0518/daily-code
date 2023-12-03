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
    INF = 200000000
    def __init__(self, is_unique = False, list_length = 5) -> None:
        print("class:", self.__class__.__name__)
        self.random_integers = []
        self.random_integers = self.get_random_num_list(is_unique, list_length)

    def get_random_num_list(self, is_unique = False, list_length = 5):
        if is_unique is True:
            # 重複のないランダムな整数のリストを生成
            unique_numbers = random.sample(range(1, 10), list_length)
            print(unique_numbers)
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
                param1 = int(sys.argv[1])
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

# 

class LinerSearch(BruteForce):
    """_summary_

    Args:
        BruteForce (_type_): _description_
    """
    def __init__(self, is_unique = False, list_length = 5) -> None:
        super().__init__()
    
    def search(self):
        """
        python3 design_technique/brute_force.py 5

        Returns:
            _type_: _description_
        """
        found_id = self.found_id()
        print(found_id)
        if found_id < 0:
            return False
        return True

    def get_found_id(self):
        search_value = self.get_value()
        # print(search_value)
        for i, v in enumerate(self.random_integers):
            if v == search_value:
                return i
        return -1

    def get_min_value(self):
        # min_value = self.random_integers[0]
        min_value = self.INF
        for i in self.random_integers:
            if min_value > i:
                min_value = i
        return min_value

    def search_pair(self):
        list1 = self.random_integers
        list2 = self.get_random_num_list()
        threshold = self.get_value()
        min_value = self.INF
        print("Thershold is %d." % (threshold))
        for i in list1:
            for j in list2:
                target = i + j
                print("{},{}".format(target, min_value))
                if target < threshold:
                    continue
                if target < min_value:
                    min_value = target
                    print("Min value is %d." % (min_value))
        return min_value

    def sum_subset(self):    
        value = self.get_value()
        self._get_subset()
        return value
    
    def _get_subset(self):
        list1 = self.get_random_num_list(True, 3)
        subset_size = 2
        subset_list = random.sample(list1, subset_size)
        print(subset_list)
        return subset_list

    def binary_representation_subset(self):
        subset_list = self._get_subset()
        

    def _bit_search(self):
        return 0        
        
# wipdoc
class BitSearch(BruteForce):
    """partial sum

    Args:
        BruteForce (_type_): _description_
    """
    def __init__(self) -> None:
        super().__init__()

def exercise31():
    found_id = -1
    a_list = [1 ,3, 4, 4 ,3 ,3 ,3 ,3, 2, 2, 2]
    v = 3
    for i in range(len(a_list)):
        if a_list[i] == v:
            found_id = i
            # break
    print(found_id)

def exercise32():
    """
    Design an O(N) algorithm to determine 
    how many integers are present among N integers a0, a1, ..., an-1.
    """
    inc_v = 0
    v = 4
    a_list = [1 ,3, 4, 4 ,3 ,3 ,3 ,3, 2, 2, 2]
    for i in range(len(a_list)):
        if a_list[i] == v:
            inc_v = inc_v + 1
            # break
    print(inc_v)
    
def exercise33():
    """
    Design an O(N) algorithm to find the maximum difference 
    between any two distinct integers among N different integers, a0 through an-1.
    """
    brute_force = BruteForce(False, 10)
    # get random integer array
    a_list = brute_force.random_integers
    max_difference = -1 * brute_force.INF
    
    print(a_list)
    for i in range(len(a_list)):
        for j in range(i + 1, len(a_list)):
            calc_value = a_list[i] - a_list[j]
            calc_value = abs(calc_value)
            print("%d - %d = %d,differnce:%d." % (a_list[i] ,a_list[j], calc_value, max_difference))
            if calc_value > max_difference:
                max_difference = calc_value
    print("max value:%d" % max_difference)
    
    # for i in range(1, len(a_list)):
    #     calc_value = a_list[i] - a_list[-1]
    #     calc_value = abs(calc_value)
    #     print("calc_value:%d,differnce:%d." % (calc_value, differnce))
    #     if calc_value > differnce:
    #         differnce = calc_value
    # print(differnce)

    
def main():
    # exercise31()
    # exercise32()
    exercise33()
    
if __name__ == "__main__":
    # 自身のファイル名を取得し、表示する
    script_name = os.path.basename(__file__)
    print(script_name)
    main()

