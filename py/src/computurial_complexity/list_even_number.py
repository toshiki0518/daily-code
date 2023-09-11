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