def _try(divisor=10, dividend =0):
    try:
        result = divisor / dividend
        print(result)
    except ZeroDivisionError:
        print("ゼロで割ることはできません。")
    finally:
        print("最後に実行される処理")
        
def main():
    _try(10, 2)
    _try(10, 0)

if __name__ == "__main__":
    main()