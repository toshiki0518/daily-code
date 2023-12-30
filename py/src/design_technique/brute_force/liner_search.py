import os
import random
from brute_class import BruteForce

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

    def found_id(self):
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
        pass
        subset_list = self._get_subset()

    def brute_force_search_pair(self):
        """
        python3 basic.py 5 10
        Nこの整数a0,a1,an-1と正の整数Wが与えられます
        いくつかの整数を選んで総和をWとすることができるかどうかを判定してください。
        ビット演算を用いる
        """
        array_length = self.get_value()
        positive_number = self.get_value()
        print("array_length,positive_number:{},{}".format(array_length,positive_number))
        random_list = self.get_random_num_list(False, array_length)

        for i in range(0, len(random_list)):
            combination = {}
            combination[i] = random_list[i]
            if positive_number == sum(combination.values()):
                print("combination:{}".format(combination))
            for l in range(i, len(random_list)):
                for r in range(l + 1, len(random_list)):
                    combination[r] = random_list[r]
                    if positive_number == sum(value for value in combination.values()):
                        print("combination:{}".format(combination))


    def _bit_search(self):
        return 0        
        
def subset_to_binary(subset, elements):
    binary_rep = 0
    for element in elements:
        if element in subset:
            binary_rep |= 1 << elements.index(element)
    return bin(binary_rep)[2:].zfill(len(elements))

def test_subset_to_binary():
    # 集合と要素の定義
    elements = ['a', 'b', 'c']
    subset = ['a', 'b', 'c']

    # 部分集合を2進数で表現
    binary_representation = subset_to_binary(subset, elements)
    print(binary_representation)  # 出力: '101'

def main():
    liner_search()
    
def liner_search():
    # ls = LinerSearch()
    ls = LinerSearch(True, 8)
    # result = ls.search()
    # result = ls.get_min_value()
    # result = ls.search_pair()
    # result = ls.binary_representation_subset()
    ls.brute_force_search_pair()
    # print(result)


if __name__ == "__main__":
    # 自身のファイル名を取得し、表示する
    script_name = os.path.basename(__file__)
    print(script_name)
    main()


