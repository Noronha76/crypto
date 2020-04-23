#!/usr/bin/python


## Imports
import socket


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
    
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((ip, door))

primeira = True
while True:
    if not primeira:
        b = keep()
        if b == 0:
            break
    primeira = False
    while True:
        dados = mysocket.recv(1024)
        if not dados:
            break
        print(dados.decode('utf-8'))
        
    
mysocket.close()    
print('conexões fechadas!')