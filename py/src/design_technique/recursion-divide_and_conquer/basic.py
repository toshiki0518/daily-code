import sys
import os
import math
import random



class BruteForce:
    INF = 200000000
    def __init__(self, is_unique = False, list_length = 5) -> None:
        # print("class:", self.__class__.__name__)
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
        
class Challenge():
    
    def exercise31(self):
        found_id = -1
        a_list = [1 ,3, 4, 4 ,3 ,3 ,3 ,3, 2, 2, 2]
        v = 3
        for i in range(len(a_list)):
            if a_list[i] == v:
                found_id = i
                # break
        print(found_id)

    def exercise32(self):
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
        
    def exercise33(self):
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

    def exercise34(self):
        """
        Design an O(N) algorithm
        to find the second smallest distinct integer among N different integers, where N >= 2.
        """
        liner_search = LinerSearch(False, 10)
        # get random integer array
        a_list = liner_search.random_integers
        smallest_value = liner_search.INF
        second_smallest_value = liner_search.INF
        
        print(a_list)
        for v in a_list:
            if v < smallest_value:
                second_smallest_value = smallest_value
                smallest_value = v
            elif v < second_smallest_value and v != smallest_value:
                smallest_value = v
        print("second_smallest_value:%d" % second_smallest_value)

    def is_even(self, num):
        return num % 2 == 0

    def exercise35(self):
        """
        Given N integers a0, a1, ..., an-1, 
        perform the following operation repeatedly until it becomes impossible: 
            replace each integer with its value divided by 2 if it is even.
        Design an algorithm to determine how many times this operation will be performed.
        """
        is_unique = False
        liner_search = LinerSearch(is_unique, 10)
        divid_count = 0
        original_list = liner_search.random_integers
        a_list = liner_search.random_integers.copy()
        has_not_odd = True
        i = 0
        # while has_not_odd:
        #     v = a_list[i]
        #     if self.is_even(v) is False:
        #         has_not_odd = False
        #         break
        #     a_list[i] = v / 2
        #     i = i + 1
        #     if i >= len(a_list):
        #         i = 0
        #         divid_count = divid_count + 1

        while True:
            for i in range(len(a_list)):
                if a_list[i] % 2 != 0:
                    if divid_count >= 1:
                        print(original_list)
                        print("divid_count:%d",divid_count)
                        print(a_list)
                    return divid_count
                    # break
                a_list[i] //= 2
            divid_count += 1



    def check_exercise35(self):
        """
        check logig about exercise35
        """
        while self.exercise35() <= 0:
            continue

    def exec_exercise36(self):
        m = 10
        n = 5
        self.exercise36(m ,n)

    def exercise36(self, m=10, n=5):
        """
        There are two integers, M and N.
        Design an O(N^2) algorithm to
        determine the number of integer solutions (X, Y, Z)
        that satisfy the conditions 0 <= X, Y, Z <= M and X + Y + Z = N.
        """
        count = 0

        for x in range(m + 1):
            for y in range(m + 1):
                z = n - x - y
                if 0 <= z <= m:
                    print(f"x:{x}, y:{y}, z:{z}")
                    count += 1

        print("Number of solutions:", count)
        return count

    def exercise36_wrong(self, m = 10, n = 5):
        """
        There are two integers, M and N. 
        Design an O(N^2) algorithm to 
        determine the number of integer solutions (X, Y, Z) 
        that satisfy the conditions 0 <= X, Y, Z <= M and X + Y + Z = N.
        """
        """
        Additionally, the algorithm in its current form has a time complexity of O(M^3), not O(N^2) as specified in the problem statement.
        """
        x = y = z =0

        while x <= m:
            while y <= m:
                while z <= m:
                    if x + y + z == n:
                        print("x:%d,y:%d,z:%d",(x, y, z))
                    z += 1
                z = 0
                y += 1
            y = 0
            x += 1
            

class Recrusive:
    def __init__(self) -> None:
        pass
    
    def func(self, N: int):
        if N == 0 :
            return 0
        return N + self.func(N - 1)

    def func2(self, N: int):
        print("N:%d",N)
        if N == 0 :
            return 0
        value = N + self.func2(N - 1)
        print("value:%d",value)
        return value

    def func3(self, N: int):
        """
        infinity loop
        """
        print("N:%d",N)
        if N == 0 :
            return 0
        value = N + self.func3(N + 1)
        print("value:%d",value)
        return value

    def func4(self, m, n):

        """
        greatest common divisor
        GCD(m,n) = GCD(n,r)

        Returns:
            _type_: _description_
        """

        print("m,n:{},{}".format(m,n))
        if n == 0:
            return m
        r = m % n
        return self.func4(n, r)


# python3 chapter_exercises.py
def main():
    recrusive = Recrusive()
    gcd = recrusive.func4(99, 48)
    print("gcd: {}".format(gcd))
    gcd = recrusive.func4(84, 24)
    print("gcd: {}".format(gcd))
    
    # basic = recrusive.func3(5)
    # print("basic: %d",basic)
    
if __name__ == "__main__":
    # 自身のファイル名を取得し、表示する
    script_name = os.path.basename(__file__)
    print(script_name)
    main()

