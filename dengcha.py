#coding:utf-8
'''
时间限制：1秒
空间限制：100768K
小易有一个长度为N的正整数数列A = {A[1], A[2], A[3]..., A[N]}。
牛博士给小易出了一个难题:
对数列A进行重新排列,使数列A满足所有的A[i] * A[i + 1](1 ≤ i ≤ N - 1)都是4的倍数。
小易现在需要判断一个数列是否可以重排之后满足牛博士的要求

输入的第一行为数列的个数t(1 ≤ t ≤ 10),
接下来每两行描述一个数列A,第一行为数列长度n(1 ≤ n ≤ 10^5)
第二行为n个正整数A[i](1 ≤ A[i] ≤ 10^9)

对于每个数列输出一行表示是否可以满足牛博士要求,如果可以输出Yes,否则输出No


输入例子1:
2
3
1 10 100
4
1 2 3 4

输出例子1:
Yes
No
'''

num = int(input())
list = []
for i in range(num):
    l = int(input())
    str = input().split()
    #str = []
    jieguo = "Yes"
    for j in range(len(str)):
        str[j] = int(str[j])
    for k in range(l-1):
        if str[k]*str[k+1]%4 != 0:
            jieguo = "No"
            break
    list.append(jieguo)  	
for m in list:
    print(m)