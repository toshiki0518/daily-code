from collections import deque
import queue
import sys
import math
import random
import datetime
import time

    
"""ハッシュテーブルを用いてデータの検索を高速化します。
計算量:O(n)
ハッシュ値の衝突=keyが同一になる
ダブルハッシュを用いたオープンアドレス法
"""
class Disctionary:
    dict={}
    dict_max = 10000
    
    
    def change_int(self, str):
        if str == 'A' : return 1
        if str == 'C' : return 2
        if str == 'G' : return 3
        if str == 'T' : return 4
        return 0
        
    def create_key(self, str):
        str_list = list('str')
        sum = 0
        p=1
        for char in len(str_list):
            print(char)
            sum += p*self.change_int(char)
        return sum
        
    def insert(self, str):
        key = self.create_key(str)
        self.dict[key] = str
        print(self.dict)
        
    def find(self, str):
        val = self.dict.get(str)
        print(val)

    def check(self, str):
        print(self.dict)

def sample():
    hash_dict = Disctionary()
    hash_dict.insert('AAA')
    hash_dict.insert('AAC')
    hash_dict.find('AAA')
    hash_dict.find('CCC')
    hash_dict.insert('CCC')
    hash_dict.find('CCC')
    
            
def main():
    print('start')
    start_time = time.time()
    print(start_time)
    # test()
    sample()
    hash_dict = Disctionary()
    # binary.exec()
    end_time = time.time()
    print(end_time - start_time)
    print('end')
        
    
if __name__ == '__main__':
    main()
