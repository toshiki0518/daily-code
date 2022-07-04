
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
        pass
    
def main():
    print('main')
    calc = Calc()
    # calc.average()
    result = calc.addup2(10)
    result = calc.addup2(9)
    result = calc.addup2(8)
    print('addup result is ', result)
    
if __name__ =='__main__':
    main()
    
# a = 0
# for i in range(1, 11):
#     a += i
# print(a)