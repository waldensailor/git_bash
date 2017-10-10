#!/usr/bin/python3
#-*- coding:utf-8- *-
import threading, time, multiprocessing
def loop():
    print("thread %s is running" % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("thread %s-----%d" % (threading.current_thread().name, n))
        time.sleep(3)
    print("thread %s is end" % threading.current_thread().name)    
'''
print("thread %s is running" % threading.current_thread().name)
t = threading.Thread(target=loop, name='loopthread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
'''




balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
        
def music(name):
    for i in range(1000):
        print("播放音乐%s第%d" % (name, i))
def game(name):
    for i in range(100):
        print("游戏￥%s￥第%d杀" % (name, i))

#t1 = threading.Thread(target=music, args=("qqmusic",))
#t2 = threading.Thread(target=game, args=("sanguosha",))
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
'''
#跑满每个cpu死循环
def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
'''