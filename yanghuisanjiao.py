#!/usr/bin/python3
#-*- coding：utf-8 -*-
'''
输出杨辉三角，用迭代器
'''
def triangles():
    a = [1]
    n = 1
    while 1:
        yield a
        b = [1]
        for i in range(len(a)):
            if i == len(a)-1:
                b.append(1)
            else:
                b.append(a[i]+a[i+1])
        a = b
g = triangles()
for i in range(20):
    print(next(g))