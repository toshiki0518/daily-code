import os
import random
import math
from brute_class import BruteForce


class BitSearch(BruteForce):
    """partial sum

    Args:
        BruteForce (_type_): _description_
    """
    def __init__(self) -> None:
        super().__init__()

    def brute_force_search_pair(self):
        """
        python3 basic.py 5 10
        Nこの整数a0,a1,an-1と正の整数Wが与えられます
        いくつかの整数を選んで総和をWとすることができるかどうかを判定してください。
        """
        array_length = self.get_value()
        positive_number = self.get_value()
        print("array_length,positive_number:{},{}".format(array_length,positive_number))
        random_list = self.get_random_num_list(False, array_length)

    def count_combinations(self):
        N = self.get_value()
        """
        N個の異なる整数が与えられた場合の組み合わせの総数を計算する関数。

        Args:
        - N: 選ぶ整数の総数

        Returns:
        - total_combinations: 組み合わせの総数
        """
        total_combinations = 0

        # 0からNまでの各kに対して、N個の整数からk個を選ぶ組み合わせの総数を計算し合算
        for k in range(N):
            # 組み合わせの計算式：N! / (k!(N-k)!)
            combination = math.factorial(N) // (math.factorial(k) * math.factorial(N - k))
            
            # 合計に加算
            total_combinations += combination

        # 結果を表示
        print(f"{N}個の整数から選ぶ組み合わせの総数: {total_combinations}通り")
        return total_combinations

    def _bit_shift(self):
        # 左シフト演算子 (<<)
        x = 1
        y = 3
        result = x << y
        print(result)  # 結果は 8 (2の3乗)

        # 右シフト演算子 (>>)
        x = 8
        y = 2
        result = x >> y
        print(result)  # 結果は 2 (8を2で割った結果)
        return 0 

    def _bit_search(self):
        return 0 

    def test_find_subset_with_sum(self, nums = [1, 2, 3, 4, 5], target_sum = 10):

        n = len(nums)
        result = []

        # 0から2^nまでの全ての部分集合を試す
        for mask in range(1 << n):
            current_subset = [nums[i] for i in range(n) if (mask & (1 << i)) > 0]
            subset_sum = sum(current_subset)

            # 和が目標の数に等しい場合、結果に追加
            if subset_sum == target_sum:
                result.append(current_subset)

        print(result)
        return result


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

def bit_search():
    bs = BitSearch()
    # bs.brute_force_search_pair()
    # bs.count_combinations()
    bs.test_find_subset_with_sum()

def main():
    bit_search()
    # liner_search()
 
if __name__ == "__main__":
    # 自身のファイル名を取得し、表示する
    script_name = os.path.basename(__file__)
    print(script_name)
    main()
    # test_subset_to_binary()

