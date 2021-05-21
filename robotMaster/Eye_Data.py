#!/usr/bin/env python
# -*- coding:utf-8 -*-
#D:\Coding\Python\20210507
import socket
import json
import time
import cv2

def windows_split(x,y):
    if (x > 0 and y >0) and (x < 640 and y < 310):
        print("1")
    elif (x > 640 and y > 0) and (x < 1280 and y < 310):
        print("2")
    elif (x > 1280 and y > 0) and (x < 1920 and y < 310):
        print("3")
    elif (x > 0 and y > 310) and (x < 640 and y < 620):
        print("4")
    elif (x > 640 and y > 310) and (x < 1280 and y < 620):
        print("5")
    elif (x > 1280 and y > 310) and (x < 1920 and y < 620):
        print("6")
    elif (x > 0 and y > 620) and (x < 640 and y < 930):
        print("7")
    elif (x > 640 and y > 620) and (x < 1280 and y < 930):
        print("8")
    elif (x > 1280 and y > 620) and (x < 1920 and y < 930):
        print("9")
    elif (x > 0 and y > 930) and (x <640 and y < 1080):
        print("10")
    elif (x > 640 and y > 930) and (x < 1280 and y < 1080):
        print("11")
    elif (x > 1280 and y > 930) and (x < 1920 and y < 1080):
        print("12")

ip_port = ('127.0.0.1', 6555)
s = socket.socket()     # 创建套接字
s.connect(ip_port)      # 连接服务器
values = []
out_win = 'img'
#out_put = cv2.imread('yidong222.png',cv2.IMREAD_UNCHANGED)[:,:,3]
img1 = cv2.imread('yidong222.png')
img2 = cv2.imread('111.png')
cv2.namedWindow(out_win, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(out_win, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
dst=cv2.addWeighted(img1,0.7,img2,0.7,0)
cv2.imshow(out_win, dst)


while True:     # 通过一个死循环不断接收用户输入，并发送给服务器
    # inp = input("请输入要发送的信息： ").strip()
    # if not inp:     # 防止输入空信息，导致异常退出
    #     continue
    # s.sendall(inp.encode())

    # if inp == "exit":   # 如果输入的是‘exit’，表示断开连接
    #     print("结束通信！")
    #     break
    s.sendall('values'.encode())
    
    server_reply = s.recv(4096).decode()
    server_reply = json.loads(server_reply)
    if server_reply["values"]["frame"]["avg"]["x"] == 0 or server_reply["values"]["frame"]["avg"]["y"] == 0:
        continue

    # print(server_reply["values"]["frame"]["avg"]['x'])
    x = server_reply["values"]["frame"]["avg"]['x']
    y = server_reply["values"]["frame"]["avg"]['y']
    windows_split(x,y)
    #print("x: ",x," y: ",y)
    c = cv2.waitKey(1)
    if c == ord('q'):
        break
    #values.append(server_reply)
    #print(len(values))
    # if(len(values) > 10):
    #     break
# json_str = json.loads(values[1])
# print(json_str["values"]["frame"]["avg"])

s.close()       # 关闭连接
