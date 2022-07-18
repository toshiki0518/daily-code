
from unittest import result


class Calc:
    def __init__(self) -> None:
        pass

    def average(self):
        scores =[70, 98, 92, 88, 64]
        total_score = 0
        for score in scores:
            total_score += score
        average_score = total_score / len(scores)
        print('average is ', average_score)
        
    def addup(self, num):
        sum=0
        
        for i in range(num + 1):
            sum += i
        return sum

    def addup2(self, num):
        f = 1 + num
        print(f)
        f *= num/2
        print(f)
        return int(f)
    
    def kk(self):
        """_summary_

        Returns:
            int : rescult calcuration multiply 1 - 9
        """
        result=0
        for i in range(1,10):
            calc_list = []
            for j in range(1,10):
                calc = i*j
                result += calc
                k="{}x{}={:2d}".format(i, j, calc)
                calc_list.append(k)
            print(calc_list)
        return result
    
    def prime_number(self):
        prime_list=[]
        for i in range(2,101):
            h = i//2 # 割り算の整数部（整数除算）: //演算子
            f = True
            for j in range(2, h+1):
                if i % j == 0:
                    print("i:{},j:{}".format(i, j))
                    f = False
                    break
            if f==True:
                prime_list.append(i)
        print(prime_list)
    
    def factorial(self):
        result = 10
        for i in range(9, 0, -1):
            result *= i
            print("i:,{}result:{}".format(i, result))
        return result
        
    def factorial2(self, n = 10):
        result=0
        if n==0:
            result = 1
        else:
            result = n * self.factorial2(n-1)
        print("result:{},n:{}".format(result,n))
        return result
        
def main():
    print('main')
    calc = Calc()
    # calc.average()
    # result = calc.addup2(10)
    # result = calc.kk()
    # print('kk result is ', result)
    # calc.prime_number()
    result = calc.factorial2()
    print('factorial result is ', result)
    
    
if __name__ =='__main__':
    main()
    
# a = 0
# for i in range(1, 11):
#     a += i
# print(a)