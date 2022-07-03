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
    dict_max = 100
    command_max = 0
    find_list={}
    

    def __init__(self, length = None):
        try:
            if length is not None:
                self.command_max = length
            else:
                self.command_max = int(input('input number '))
                if(self.command_max > self.dict_max):
                    self.command_max = self.dict_max
        except Exception as e:
            print(e)
        else:
            self.create_dict()
        
    def create_dict(self):
        """
        空の辞書を生成
        """
        for index in range(self.command_max):
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
            sum += p*self.change_int(char)
        return sum
        
    def hash1(self, key):
        return key % len(self.dict)
        
    def hash2(self, key):
        return 1 + (key % (len(self.dict) - 1) )
        

    def create_hash_key(self, key, index):
        """_summary_

        Args:
            key (int): _description_
            index (int): _description_

        Returns:
            _type_: _description_
        """
        key1 = self.hash1(key) + index
        key2 = self.hash2(key)
        hash_key = (key1 * key2) % len(self.dict)
        return hash_key
    
    def insert(self, str):
        isFound, hash = self.find(str) 
        # print(isFound)
        # print(hash)
        if not isFound:
            self.dict[hash] = str
            # self.dict.update(hash=str)
            
    def find(self, str):
        key = self.change_key_int(str)
        cnt = 0
        while True:
            h = self.create_hash_key(key, cnt)
            print('h %d, key %d, cnt %d, str %s' % (h, key, cnt, str))
            if self.dict[h] == str:
                # 重複
                return True, h
            if self.dict[h] is None or len(self.dict[h]) == 0:
                # 取得できないなら
                return False, h
            cnt += 1
            # return False,0

    def check(self, str):
        print(self.dict)

    def exec_command(self, command, value):
        # print('command %s, value %s' % (command, value))
        if command.startswith('insert'):
            self.insert(value)
        else:
            self.find(value)
            
def sample():
    inputs = [
        'insert AAA',
        'insert AAC',
        'find AAA',
        'find CCC',
        'insert CCC',
        'find CCC',
        'insert AC',
        'insert G',
        'find AC',
        'find G',
    ]
    sample_dict = Disctionary(len(inputs))
    for input in inputs:
        command, value = input.split()
        sample_dict.exec_command(command, value)
            
    print(sample_dict.dict)
    
def main():
    print('start')
    start_time = time.time()
    print(start_time)
    sample()
    # hash_dict = Disctionary()
    # for n in range(len(hash_dict.dict)):
    #     command, value = input('input command ').split()
    #     hash_dict.exec_command(command, value)
    end_time = time.time()
    print(end_time)
    print(end_time - start_time)
    print('end')
        
    
if __name__ == '__main__':
    main()
