import sys

# sys.argv[0] には実行したスクリプトのファイル名が含まれています
# sys.argv[1] 以降には渡されたコマンドライン引数が含まれています

# 例: python3 script.py arg1 arg2
# sys.argv[0] = 'script.py'
# sys.argv[1] = 'arg1'
# sys.argv[2] = 'arg2'

# パラメータを取得
if len(sys.argv) > 1:
    param1 = sys.argv[1]
    param2 = sys.argv[2]
    # 以降のコードで param1 と param2 を使用できます

print(param1)
print(param2)