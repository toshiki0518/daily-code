import sys
import os
import math
def cal_dist(x1: float, y1: float, x2: float, y2: float):
    print(x1,y1,x2,y2)
    x = (x1 - x2 )
    y = (y1 - y2 )
    return math.sqrt(x**2 + y**2)
    

def closest_point():
    n = get_value()  # 配列の長さ
    x_list = []  # 空のリストを作成

    # N個の要素を追加
    for i in range(n):
        x_list.append(i)

    y_list = [i for i in range(n)]

    minimun_dist: float = 10000000.0

    for i in range(n):
        for j in range(i + 1, n):
            dist: float = cal_dist(x_list[i], y_list[i], x_list[j], y_list[j])
            if dist <= minimun_dist:
                minimun_dist = dist
                # print(minimun_dist)
    print(minimun_dist)


def get_value():
    if len(sys.argv) > 1:
        try:
            param1 = int(sys.argv[1])
            return param1
        except ValueError:
            print('value error')
            return 0
    else:
        print('value error')
        return 0
    


# python3 computurial_complexity/list_even_number.py 10
def main():
    closest_point()

if __name__ == "__main__":
    # 自身のファイル名を取得し、表示する
    script_name = os.path.basename(__file__)
    print(script_name)
    main()

