import sys
import os
import math
import random
import numpy as np

class Challenge():
    def __init__(self) -> None:
        pass    


class Recrusive:
    def __init__(self) -> None:
        self.func_cnt = 0
        self.answer_memos = [-1] * 50
        self.memo_cnt = 0
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

    def func5(self, n, position = ""):

        self.func_cnt += 1
        """
        fibo
        """
        if n == 0:
            print("position,n,value:{},{},{}".format(position,n,0))
            return 0
        elif n == 1:
            print("position,n,value:{},{},{}".format(position,n,1))
            return 1
        value = self.func5(n - 1, position + "left") + self.func5(n - 2, position + "right")
        print("position,n,value:{},{},{}".format(position,n,value))
        return value

    def func6(self, n, position = ""):
        num = 50
        f = np.zeros(num)
        f[0] = 0
        f[1] = 1
        for i in range(2, num):
            f[i] = f[i - 1] + f[i -2]
            print("n,f[n]:{},{}".format(i, f[i]))
            self.func_cnt += 1


    def func7(self, n, position = ""):
        # ベースケース
        if n == 0:
            self.func_cnt += 1
            return 0
        elif n ==1:
            self.func_cnt += 1
            return 1
        # メモがあればそれを使用
        if self.answer_memos[n] != -1 :
            print("answer_memos:{}".format(self.answer_memos[n]))
            self.memo_cnt += 1
            print("memo:{}".format(self.memo_cnt))
            return self.answer_memos[n]
        self.func_cnt += 1
        print("n:{}".format(n))
        value = self.func7(n - 1, "left") + self.func7(n - 2, "right")
        self.answer_memos[n] = value
        return value



# python3 bacic.py
def main():
    recrusive = Recrusive()
    # recrusive.func7(49)
    recrusive.func7(6)
    print("calc cnt:{}".format(recrusive.func_cnt))
    for v in recrusive.answer_memos:
        print("v:{}".format(v))

    # recrusive.func6(6)
    # print("calc cnt:{}".format(recrusive.func_cnt))
    # recrusive.func5(6)
    # print("calc cnt:{}".format(recrusive.func_cnt))
    # gcd = recrusive.func4(99, 48)
    # print("gcd: {}".format(gcd))
    # gcd = recrusive.func4(84, 24)
    # print("gcd: {}".format(gcd))
    
    # basic = recrusive.func3(5)
    # print("basic: %d",basic)
    
if __name__ == "__main__":
    # 自身のファイル名を取得し、表示する
    script_name = os.path.basename(__file__)
    print(script_name)
    main()

