#!/usr/bin/python
# -*- coding: utf-8 -*-

## No Python 2, em vez da função input(), utilizamos a função raw_input() para pegar a entrada do usuário como string
## AF_INET -> IPv4, AF_INET6 -> IPv6 
## SOCK_STREAM -> TCP, SOCK_DGRAM -> UDP

## Imports
import socket
import time


## Funções
def keep():
    while True:
        try:
            b = int(input("digite 0 para cancelar e 1 para continuar : "))
            if b < 2:
                break
            print("caracter inválido!")
        except:
            print("caracter inválido!")
            print("encerrando operação...")
            b = 0
            break
    return b

def ipdoor():
    i = input("IP : ")
    if i == "":
        i = "127.0.0.1"
        print('IP definido: 127.0.0.1')
    elif len(ip) > 15:
        i = "127.0.0.1"
        print('IP definido: 127.0.0.1')
    elif len(ip) < 7:
        i = "127.0.0.1"
        print('IP definido: 127.0.0.1')
    try:
        d = int(input("Porta : "))
    except:
        d = 12345
        print('Porta definida : 12345')
    if d > 56000 or d < 1024:
        d = 12345
        print('Porta definida : 12345')
    return i, d


## Main
ip, door = ipdoor()
print('Tentando conectar no IP {0} Porta {1}...'.format(ip,door))

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.bind((ip, door))
mysocket.listen(1)
connection, address = mysocket.accept()
print('Conectado com',address)
while True:
    name = input('Nome do arquivo : ')
    if name == '':
        name = 'hino.txt'
        print('Nome do arquivo : hino.txt')
    try:
        arq = open(name)
        print('Arquivo aberto!')
        time.sleep(1)
        texto = arq.read()
        palavras = texto.split()
        for i in palavras:
            print(i)
        #bug = 0
        #for i in palavras:
            connection.send(i.encode('utf-8')) # connection.sendto(i.encode('ascii')) => bug=0 connection.sendall(i.encode('ascii')) => bug=5
        #    bug += 1
        arq.close()
    except:
        print("Não foi possível abrir o arquivo")
        print('bug no ciclo : ',bug)
    b = keep()
    if b == 0:
        break
print("fechando conexão...")
connection.close()
mysocket.close()
print('conexões fechadas!')
        
        