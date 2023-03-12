print(6 % 3)
print(7 % 3)

def fizz_buzz(n):
    for i in range(1, n+1):
        if (i % 15== 0):
            print("FizzBuzz:%d" %i)
            continue
        if (i % 5 == 0):
            print("Buzz:%d" %i)
            continue
        if (i % 3 == 0):
            print("Fizz:%d" %i)
            continue
        print(i)

print(fizz_buzz(100))