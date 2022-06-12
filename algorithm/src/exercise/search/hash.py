from calendar import c
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
    dict_max = 0
    

    def __init__(self):
        self.dict_max = int(input('input number'))
        self.create_dict()
        
    def create_dict(self):
        """
        空の辞書を生成
        """
        for index in range(self.dict_max):
            self.dict[index] = None
        print('len(self.dict) is %d' % len(self.dict))
        
    
    def change_int(self, str):
        if str == 'A' : return 1
        if str == 'C' : return 2
        if str == 'G' : return 3
        if str == 'T' : return 4
        return 0
        
    def change_key_int(self, str):
        sum = 0
        p=1
        for char in str:
            print(char)
            sum += p*self.change_int(char)
        return sum
        
    def hash1(self, key):
        return key % len(self.dict)
        
    def hash2s(self, key):
        return 1 + (key % (len(self.dict) - 1) )
        
    def insert(self, str):
        key = self.change_key_int(str)
        # while True:            
        self.dict[key] = str
        print(self.dict)
        
    def find(self, str):
        val = self.dict.get(str)
        print(val)

    def check(self, str):
        print(self.dict)

    def sample(self):
        hash_dict = self
        
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
    hash_dict = Disctionary()
    hash_dict.sample()
    
    hash_dict = Disctionary()
    # binary.exec()
    end_time = time.time()
    print(end_time - start_time)
    print('end')
        
    
if __name__ == '__main__':
    main()
