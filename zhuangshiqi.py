#!/usr/bin/python3
#coding:utf-8
'''
装饰其的作用：
之前的函数不能随便改动，但是需要添加新功能
'''

def xiaomin(name):
    def zhongjian(func):
        def zuizhong(*arg, **kw):
            print("%s算的结果是"%name)
            return func(*arg, **kw)
        return zuizhong
    return zhongjian
def qnd(func):
    def wc():
        print("嘿嘿，我调用了装饰器")
        return func()
    return wc
    
@qnd    
def name():
    print("我是name函数")
    print("%s" % name.__name__)
    
@xiaomin("huazai")   
def add(a, b):
    print(a+b)
    
#name()
add(4, 6)