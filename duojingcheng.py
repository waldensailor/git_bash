#coding:utf-8
'''
#fork在windows下没有该功能
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
    
  
    
from multiprocessing import Process
from multiprocessing import Pool
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
    
    

import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
''' 
import subprocess, time
from multiprocessing import Process
import threading

'''

def hello():
    a = 0
    for i in range(10000000):
        a = a + i
        #time.sleep(0.000001)
        a = a - i
    print(a)
    print(id(a))
p1 = Process(target=hello)
p2 = Process(target=hello)
p1.start()
p2.start()
p1.join()
p2.join()

'''
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.name
    age = local_school.age
    ch = local_school.ch
    print('Hello, %s 我年龄%d 谁 %d个孩子(in %s)' % (std, age, ch, threading.current_thread().name))

def process_thread(name, age, chrildnum):
    # 绑定ThreadLocal的student:
    local_school.name = name
    local_school.age = age
    local_school.ch = chrildnum
    
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',32,3), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',12,0), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()