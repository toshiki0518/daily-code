# -*- coding: utf-8 -*-
# 整数の入力
# a = int(input())
# スペース区切りの整数の入力
b, c = map(int, input().split())

# 出力
# print("{}".format(b * c))
a = b * c
if a % 2 == 0:
    print("Even")
else:
    print("Odd")

###
# 1
# 2 3 
# test 
