import random

total= 100
class Start:
    def output(self):
        a=2021
        print(a)

    def input(self):
        a= input("input string:")
        print(a)
    
    def variable1(self):
        a=1
        s="Python"
        data="アルゴリズム"
        print(a,s,data)

    def variable2(self):
        a=1
        n=1
        print("n has init value ",n)
        n=20
        print("n has second value ",n)
        n=n + 80
        print("n has third value ",n)
        n= n -100
        print("n has forth value ",n)

    def convert1(self):
        s="100"
        print(s+s)
        i = int(s)
        print(i+i)

    def convert2(self):
        f=3.14
        print(f+f)
        s = "test:" + str(f)
        print(s)

    def condition1(self):
        n=-1
        n=0
        n=1
        if n == 0:
            print("n is zero")
        if n > 0:
            print("n is plus num")
        if n < 0:
            print("n is minus num")

    def loop1(self):
        for i in range(3):
            print(i)
        for i in range(1, 3):
            print(i)
        for i in range(0, 31, 10):
            print(i)
        for x in range(2):
            for y in range(3):
                print(x,y)
        
    def loop2(self):
        for i in range(10):
            if i < 2:
                print('continue')
                continue
            print(i)
            if i == 4:
                print('break')
                break
        
    def loop3(self):
        i = 10
        while i > 0:
            i=i-1
            print(i)
            
    def loop4(self):
        while True:
            s = input("input string ")
            print(s)
            if s =="":
                print('blank')
                break

    def function2(self, val):
        if val > 0:
            print(val, ': is plus')
        if val < 0:
            print(val, ': is minus')
        if val == 0:
            print(val, ': is zero')
                    
    def function3(self, val):
        v=4*3.14*val*val*val /3
        return v
                    
    def function_global(self):
        global total
        total = total + 100
                    
    def test_global(self):
        print('init value is ', total)
        self.function_global()
        print('second value is ', total)
        
    def arr(self):
        subject=['a', 'b', 'c']
        score=[1, 2, 3]
        sum=0
        for i in range(len(subject)):
            print(subject[i], score[i])
            sum += score[i]
        print(subject)
        print(score)
        print(sum)
                    
    def arr2(self):
        data=[
            [10, 30, 40, 50],
            [-11, -21, -31, -90],
            [60, 70, 80, 100, 10],
            
        ]
        print(data[0])
        print(data[1])
        print(data[2])
        print(data[0][2])
        print(data[1][0])
        print(data[2][1])

    def test1(self):
        a=10+5*8
        b=20-9/2
        print(a,b)
        
    def test2(self):
        x=4**3
        y=35//9
        z=x%y
        print(x,y,z)
        
    def test3(self):
        sum=0
        for i in range(5):
            if i == 4:
                sum = sum * 2
            else:
                sum +=1
            print(sum)
        
    def test4(self):
        a=[
            [7, 11, 3, 67, 55, 1],
            [21, 2, 14, 48, 16, 0],
            [41, 77, 98, -1, 5, 15],
            [-6, 9, 32, 87, 20, 8],
        ]
        print(a[0][0])
        print(a[2][4])
        print(a[3][5])
        
    def test_random(self):
        for i in range(5):
            r = random.randint(1, 6)
            print(r)
            r = random.randrange(100, 124, 4)
            print(r)
            r = random.choice(['a','b','c'])
            print(r)
        r=random.random()
        print(r)
            
    def main(self):
        # print("半径10cm is", val, 'cm')
        # print("半径20cm is", self.function3(20), 'cm')
        self.test_random()
    
def main():
    start =Start()
    print("test")
    start.main()
    
if __name__ == "__main__":
    main()