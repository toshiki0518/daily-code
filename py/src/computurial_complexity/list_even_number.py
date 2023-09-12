import sys
print('list_even_number')

# python3 computurial_complexity/list_even_number.py 10
def main():
    if len(sys.argv) > 1:
        try:
            param1 = int(sys.argv[1])
        except ValueError:
            param1 = 0
            print('value error')

    else:
        param1 = 0
    for i in range(0, param1 + 1, 2):
        print(i)

if __name__ == "__main__":
    main()

    """コマンドライン引数の読み取り:
len(sys.argv)はsys.argvリストの要素数を返すので、O(1)の計算量です。
コマンドライン引数が数値に変換される部分 (param1 = int(sys.argv[1])) はO(1)の計算量です。
forループ:
for i in range(0, param1 + 1, 2):のループは、0からparam1までの偶数を2つずつ増やしながら反復処理します。ループの回数はparam1 / 2回です。
したがって、forループ自体の計算量はO(param1)です。
全体の計算量はコマンドライン引数の読み取り部分とforループ部分の計算量の合計です。したがって、このプログラムの計算量はO(param1)です。

このプログラムの計算量は、param1（引数で指定された偶数の最大値）に比例して増加します。param1が大きい場合、計算量も大きくなります。ただし、コマンドライン引数の読み取りや変換部分は、param1の値に依存しないので、実行時間に対して影響は比較的小さいでしょう。
    """