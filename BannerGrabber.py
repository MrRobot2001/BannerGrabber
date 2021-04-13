#!/usr/bin/python3

import socket

def banner(Ip,port):
    s = socket.socket()
    s.connect((Ip,int(port)))
    s.settimeout(8)
    print(str(s.recv(1024)).strip('b'))

def main():
    Ip = input("Enter the IP: ")
    port = str(input("Enter the Port: "))
    banner(Ip,port)

main()