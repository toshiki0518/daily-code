import bisect
import random

class BaseBinarySearch:
    def __init__(self) -> None:
        pass

class ArrayBinarySearch(BaseBinarySearch):
    def __init__(self, search_value = 9) -> None:
        super().__init__()
        self.search_value = search_value
        self.sorted_array = [3,5,8,10,14,17,21,39]
        # print(self.sorted_array)

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
        
    def common_binary_search(self):
        """
        各整数xについて
        true/falseの２値で判定される条件Pが与えられていて
        ある整数l,r(l<r)が存在。
        ・P(l)=false
        ・P(r)=true
        ・ある整数M(l<M<=r)が存在して、x<Mなるxに対してP(x)=falseであり
        x>=Mなるxに対してP(x)=trueである
        このときD=r-lとして、二分探索法はMをO(logD)の計算量で求めることができる
        """
        left: int
        right: int
        while (right - left) > 1:
            mid = left + (right - left) / 2
            if self._p(mid):
                right = mid
            else:
                left = mid
        return right

    def _p(self, x: int) -> bool:
        pass

    def age_quiz(self, a_age=31):
        """
        a age is between 20 and 36
        you have four chanse for question that answer yes or no.
        """
        left = 20
        right = 36
        while (right - left) > 1:
            mid = left + (right - left) // 2
            if a_age < mid:
                ans = "yes"
            else:
                ans = "no"
            print("is the age less than {}? {}.".format(mid, ans))
            if a_age == left:
                print("hit!")
                break
            if ans == "yes":
                right = mid
            else:
                left = mid

        print("the age is {} !".format(left))
        print()

    def _generate_random_number(self):
        return random.randint(1, 10)
    
        
    def std_lower_bound(self, N=5, K=7):
        min_value = 20000000
        a_list = []
        b_list = []
        for _ in range(N):
            a_list.append(self._generate_random_number())
            b_list.append(self._generate_random_number())
        print(b_list)
        # bをソート
        b_list.sort()
        print(b_list)
        # aを固定して解く
        for i in range(N):
            iter = bisect()

        pass




def main():
    abs = ArrayBinarySearch()
    abs.std_lower_bound()
    return 
    abs.age_quiz()
    abs.age_quiz(34)
    abs.age_quiz(25)
    abs.age_quiz(28)
    abs.age_quiz(24)
    # abs.binary_search()
    # abs.bisect()
    # abs.exec(10)
    # abs.exec(3)
    # abs.exec(39)

    # abs.exec(-100)
    # abs.exec(9)
    # abs.exec(1000)

if __name__ == "__main__":
    main()