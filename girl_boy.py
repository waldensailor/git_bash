#!/usr/bin/python3
#-*- coding:utf-8 -*-

'''
模拟生到男孩就不允许生,最多生三个，最终的男女比例是
模拟的最终结果一直在0.5左右，选的家庭数越多，越接近
还有谁傻不拉几的说生到男孩为止会导致男女比例失调
'''
from random import choice
'''
class Family():
    chrildSum = 0
    boySum = 0
    def __init__(self):
        for i in range(5):
            self.boySum = choice([0, 1])
            self.chrildSum += 1
            if self.boySum:
                break

        
        
if __name__ == '__main__':
    boyCount = 0
    chrildCount = 0
    for i in range(100000):
        a = Family()
        chrildCount += a.chrildSum
        boyCount += a.boySum
    print("最终人数是%d" % chrildCount)
    print("男孩比例是%f" % (boyCount/chrildCount))
'''


'''
类变量跟成员变量：
1.类变量只能通过类名字来修改，通过成员变量修改的都会在实例中新建一个属性
2.当类变量重名实例变量的时候，通过实例优先返回实例变量
'''
class  A():
    a = 10
    def __init__(self, elem):
        self.a = elem
        
if __name__ == '__main__':
    
    print("类变量：A.a", A.a)
    for i in range(4):
        adc = A(i)
        adc.a = i+1
        print("成员变量：b", adc.a)
    '''
    python = A(4)
    python.a = 5
    print(A.a)
    print(python.a)
    '''