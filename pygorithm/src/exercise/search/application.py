from calendar import c
from collections import deque
import queue
import sys
import math
import random
import datetime
import time
# import numpy

    
"""ハッシュテーブルを用いてデータの検索を高速化します。
計算量:O(n)
ハッシュ値の衝突=keyが同一になる
ダブルハッシュを用いたオープンアドレス法
"""
class Logistics:
    quantity=0
    luggage=[]
    weight_average=0
    truck=dict()
    max_loadage=0
    unit_count = 0
    dict_max = 100
    command_max = 0
    find_list={}
    n=0
    k=0
    list=[]

    def __init__(self, length = None):        
        self.quantity = int(input('inuput quantity '))
        self.unit_count = int(input('inuput unit_count '))
        
    def calc_laggeage(self, quantity = None):
        total_weight = 0
        if quantity is None:
            quantity = self.quantity
            for n in range(quantity):
                num = n + 1
                total_weight += (num)
                self.luggage.append(num)
        else:
            for n in range(quantity):
                luggage_weight = int(input('input luggage weight '))
                total_weight += luggage_weight
                self.luggage.append(luggage_weight)
        # print('total_weight %d / self.unit_count %d' % (total_weight, self.unit_count))
        self.weight_average = total_weight / self.unit_count
        print('total_weight %d / self.unit_count %d, self.weight_average%d' % (total_weight, self.unit_count, self.weight_average))
        print(self.luggage)
        
    def sample(self):
        self.calc_laggeage()
        self.load_luggage()
        print(self.truck)
        print(self.max_loadage)
            
    def check(self):
        self.calc_laggeage(self.quantity)
        self.load_luggage()
        print(self.truck)
        print(self.max_loadage)
            
    def load_luggage(self):
        track_number=1
        weight=0
        for luggage in self.luggage:
            is_use, weight = self.calc_loadage(weight, luggage)
            if is_use is None:
                continue
            # 次のトラックへ
            self.truck[track_number] = weight
            # print('track_number %d, weight %d, luggage %d' % (track_number, weight, luggage))
            weight = 0 if is_use is False else luggage
            print('track_number %d, weight %d, luggage %d' % (track_number, weight, luggage))
            track_number+=1
        
    def calc_loadage(self, weight, luggage):
        """
        最大積載量を計算する
        すべての重さの荷物 / トラック台数:ng
        1.足した結果が平均を超えているか
        2.足した結果と平均の差
        足す前と平均の差
        でより近いほう

        Args:
            weight (_type_): _description_
            luggage (_type_): _description_

        Returns:
            _type_: _description_
        """
        after_weight = weight + luggage
        if after_weight >= self.weight_average :
            print('weight %d, luggage %d, after_weight %d' % (weight, luggage, after_weight))
            diff_after_weight = after_weight - self.weight_average
            diff_weight = self.weight_average - weight
            result=0
            print('diff_after_weight %d, diff_weight %d ' % (diff_after_weight, diff_weight))
            use_before = False
            if diff_after_weight < diff_weight:
                result = after_weight
                use_before = False
            else:
                use_before = True
                result = weight
            if result >= self.max_loadage:
                 self.max_loadage = result
            print('result %f' % result)
            return use_before, result
        return None, after_weight
            
    def answer(self):
        for i in range(self.quantity):
            # print(i)
            kg = int(input('input weight:'))
            self.list.append(kg)
        ans = self.solve()
        print('answer is %d' % ans)
        
    def solve(self):
        left = 0
        right = 100000 * 10000
        mid: int
        while (right - left) > 1:
            mid = (left + right) /2 
            print('right:%d,left:%d,mid:%d' % (right,left,mid))
            val = self.calc(mid) # mid == 最大積載量
            print('val:%d' % (val))
            if( val >= self.quantity):
                right = mid
            else:
                left = mid
        return right
        
    def calc(self, loadage):
        i = 0
        for j in range(self.unit_count):
            s = 0
            while (s + self.list[i] <= loadage):
                s += self.list[i]
                i += 1
                print('j:%d,i:%d,s:%d,loadage:%d' % (j,i,s,loadage))
                if i == self.quantity:
                    return self.quantity
        print('i:%d' % (i))
        return i
        
def main():
    print('start')
    start_time = time.time()
    print(start_time)
    logistics = Logistics()
    # logistics.sample()
    # logistics.check()
    logistics.answer()
    end_time = time.time()
    print(end_time)
    print(end_time - start_time)
    print('end')
        
    
if __name__ == '__main__':
    main()
