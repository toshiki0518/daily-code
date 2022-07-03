# stack is last in first out
# from asyncio.windows_events import NULL
from collections import deque
from re import A
import sys
import operator as op


def main():
    print ('start')
    #    stackPush()
    # stackPop()
    # stackPopDeque()
    # testCheckArrayLength()
    # stackPopEnd()
    testReversePolishNotion()
    # testPrintFormat()

def stackPush():
    print(sys._getframe().f_code.co_name)
    facts = ['1st','2nd']
    facts.append('3rd')
    # 配列のままセットされる
    facts.append(['4th','5th'])
    facts.extend(['4th','5th'])
    for fact in facts:
        print(fact)

def stackPopEnd():
    print(sys._getframe().f_code.co_name)
    facts = []
    facts.append(1) 
    facts = facts + [2] 
    facts +=[3] 
    print(facts.pop())
    print(facts.pop())
    print(facts.pop())
    
def stackPop():
    print(sys._getframe().f_code.co_name)
    inserts = ['1st','2nd']
    facts = []
    facts.append('3rd')

    # 配列のままセットされる
    facts = facts + ['d']
    facts += ['d2']
    facts.append(['4th','5th'])
    facts.extend(['4th','5th'])
    # https://wiki.python.org/moin/TimeComplexity
    # 非効率的
    facts.insert(0, inserts)
    print(facts[-1])

def stackPopDeque():
    print(sys._getframe().f_code.co_name)
    inserts = ['1st','2nd']
    facts = deque()
    facts.append('3rd')
    # https://wiki.python.org/moin/TimeComplexity
    # 非効率的
    facts.insert(0, inserts)

    # 配列のままセットされる
    facts.append(['4th','5th'])
    facts.extend(['4th','5th'])
    print(facts.pop())



def checkArrayLength(checkedList):
    """_summary_
    print result that check list is empty or not empty
    Args:
        checkedList (collection.deque): _description_
    """
    print(sys._getframe().f_code.co_name)
    if len(checkedList) is checkedList.maxlen:
        print('list is full')
        print('max length is %d' % (len(checkedList)))
    elif checkedList:
        print('not empty')
        print('length is %d' % (len(checkedList)))
    else:
        print('empty')

def testCheckArrayLength():
    checkedList =deque([], 2)
    checkArrayLength(checkedList)
    checkedList.append('test')
    checkArrayLength(checkedList)
    checkedList.append('test2')
    print (len(checkedList))
    checkArrayLength(checkedList)

def testPrintFormat():
    print(sys._getframe().f_code.co_name)
    a = 'abc'
    b = 5
    print('test %d' % b)
    
    
def testReversePolishNotion():
    print(sys._getframe().f_code.co_name)
    testStackValue = [1,2,'+',3,4,'-','*']
    # testStackValue = [10,22,'+']
    reversePolishNotion(testStackValue)

def reversePolishNotion(targetList):
    """_summary_
    逆ポーランド記法の計算
    記号→記号 = 計算しない
    記号→数字 = 計算しない
    数字→数字 = 計算
    Args:
        targetList (list): _description_
    """
    print(sys._getframe().f_code.co_name)
    calcValue = 0
    symbolList = []
    calcList = []
    for val in targetList:
        # print(type(val) is int)
        print(val)
        if type(val) is not int:            
            valB = calcList.pop()
            valA = calcList.pop()
            resultVal = calcPolishNotion(valA, valB, val)
            calcList.append(resultVal)
        else:
            calcList.append(val)
                
    print(calcList.pop())

def calcPolishNotion(m, n, ope):
    print('formula is %d %s %d' % (m, ope, n))
    if ope == '+' :
        return op.add(m, n)
    elif ope == '*' :
        return op.mul(m, n)
    elif ope == '-':
        return op.sub(m, n)
    else:
        return op.truediv(m, n)


if __name__ == '__main__':
    main()
