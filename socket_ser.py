#!/usr/bin/python3
#coding:utf-8

import socket, threading, time

def tcplink(sock, addr):
    time.sleep(2)
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#设置监听端口
s.bind(("127.0.0.1", 9999))
#设置等待的数量
s.listen(5)
print('Waiting for connection...')

n = 0
while True:

    # 等待接受一个新连接,该函数立
    sock, addr = s.accept()
    time.sleep(2)
    print("链接建立好了")
    #print(sock, addr)
    # 创建新线程来处理TCP连接:    
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
    print("the %dth new link create" % n)
    n += 1
    
