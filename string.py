'''
#接受两个字符串，按照8位切割
str1 = input("nu1")
str2 = input("nu2")
strlist = [str1, str2]
for str in strlist:
    leng = len(str)
    num = leng // 8
    yushu = leng % 8
    for n in range(num):
        lower = n * 8
        upper = (n + 1) * 8
        print(str[(n*8):(8*n+8)])
    if yushu:
        buquan = 8 - yushu
        last_str = str[(num*8):]
        for i in range(buquan):
            last_str += "0"
        print(last_str)
'''

'''
#接受两个16进制数字，转换为10进制数字
str1 = input("")
str2 = input("")
list_a = [str1, str2]
dict_num = {"0": 0, "1": 1, "2": 2,
        "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8,
        "9": 9, "a": 10, "b": 11,
        "c": 12, "d": 13, "e": 14,
        "f": 15, "A":10, "B": 11,
        "C": 12, "D":13, "E": 14,
        " F": 15,}
for i in list_a:
    this_str = i[2:]
    length = len(this_str)
    num = 0
    for char in this_str:
        length -= 1
        char_value = dict_num[char]
        num += char_value*(16**(length))
    print(num)
    '''
'''
#输入一个浮点数返回他的四舍五入整数
value = input("")
value = float(value)
yushu = (10*value)%10
shan = (10*value)//10
if yushu > 5:
    shan += 1
print(shan)
'''
'''
count = input()
count = int(count)
dict_h = {}
for i in range(count):
    a = input("")
    list_a = a.split(" ", 2)
    if list_a[0] in dict_h:
        dict_h[list_a[0]] += int(list_a[1])
    else:
        dict_h[list_a[0]] = int(list_a[1])
for key, value in dict_h.items():
    print(key, value)
 '''   
'''
import sys
count = int(input())
dict_h = {}
for i in range(count):
    key, value = map(int, input().split(" ",2))
    if key in dict_h.keys():
        dict_h[key] += value
    else:
        dict_h[key] = value
for j in dict_h:
    print(j, dict_h[j])
'''

'''
num = int(input())
str = []
strl = ""

def ou(num, str):
    num -= 2
    num /= 2
    str.append("2")
    #print(str)
    return num
def ji(num, str):
    num -= 1       
    num /= 2
    str.append("1")        
    return num

while num:       
    if num%2==1:
        num = ji(num, str)
        #print("fdfd")
    else:
        num = ou(num, str)
str.reverse()
for i in str:
    strl += i
print(strl)
'''

import decimal
str = input()
index = str[0]
count = 1
for i in str:
    if not index == i:
        index = i
        count += 1
length = len(str)
last = length/count

def liangwei(sum):
    yushu = int((sum *1000)%10)
    if yushu < 5:
        yushu = 0
    else:
        yushu = 1
    return (int(sum*100)+yushu)/100
hello = round(liangwei(last), 2)
x = decimal.Decimal(repr(hello).quantize(Decimal('0.00')))
print(x)