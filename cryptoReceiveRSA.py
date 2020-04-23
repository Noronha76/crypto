#!/usr/bin/python


## Imports
import socket
from ast import literal_eval


## Funções

'''
Função modular entre dois números
'''
def mod(a,b): # mod function
    if(a<b):
        return a
    else:
        c=a%b
        return c


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

def listint(a):
    b = a.split()
    d = []
    f = []
    for ii in b:
        c = ""
        for i in ii:
            if i == "'":
                e = ""
            elif i == "[":
                e = ""
            elif i == "]":
                e = ""
            elif i == ",":
                e = ""
            elif i == "":
                e = ""
            else:
                c = c + i
        d.append(c)
    for i in d:
        f.append(int(i))
    return f


'''
Descriptografa um texto criptografado
'''
def descifra(cifra_str,n,d):
    try:
        cifra = literal_eval(cifra_str)
    except:
        try:
            cifra = listint(cifra_str)
        except:
            cifra = [0]
    lista = []
    i = 0
    tamanho = len(cifra)
    # texto=cifra ^ d mod n
    try:
        while i < tamanho:
            result = int(cifra[i])**d
            texto = mod(result,n)
            letra = chr(texto)
            lista.append(letra)
            i += 1
        strng = str('')
        strng1 = strng.join(lista)
        return strng1
    except:
        strng1 = ''
        return strng1

## Main
ip, door = ipdoor()
    
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((ip, door))

n_ = mysocket.recv(1024)
d_ = mysocket.recv(1024)
n = int(n_.decode('utf-8'))
d = int(d_.decode('utf-8'))
print('Chaves recebidas')
primeira = True
while True:
    if not primeira:
        b = keep()
        if b == 0:
            break
    primeira = False
    while True:
        text_rec = mysocket.recv(1024)
        text_cipher = text_rec.decode('utf-8')
        #print(type(text_cipher))
        original_text = descifra(text_cipher,n,d)
        #if not original_text:
        if not text_cipher:
            break
        print(text_cipher)
        print(original_text)
        
    
mysocket.close()    
print('conexões fechadas!')