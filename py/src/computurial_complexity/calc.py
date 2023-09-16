import sys
import os
import math
import time
import datetime
def main():
    num = 10
    time = 9
    val = num**time
    count = 0
    print(datetime.datetime.now())
    for i in range(val):
        count += 1
    print(datetime.datetime.now())
    print(count)
    

if __name__ == "__main__":
    # 自身のファイル名を取得し、表示する
    script_name = os.path.basename(__file__)
    print(script_name)
    main()

