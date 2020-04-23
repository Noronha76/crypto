#!/usr/bin/python
# -*- coding: utf-8 -*-

## No Python 2, em vez da função input(), utilizamos a função raw_input() para pegar a entrada do usuário como string
## AF_INET -> IPv4, AF_INET6 -> IPv6 
## SOCK_STREAM -> TCP, SOCK_DGRAM -> UDP

## Imports
import socket
import time
import random


## Funções
'''
Calcula o totiente do numero primo
'''
def totient(number): 
    if(prime(number)):
        return number-1
    else:
        return False

    
'''
Verifica se um numero gerado é primo
'''
# it isnt the best method to compute prime numbers
def prime(n): # check if the number is prime
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n%2 == 0 or n%3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n%i == 0 or n%(i+2) == 0):
           return False
        i+=6
    return True



'''
Gera um numero aleatório E, sasfazendo as condições
'''
def generate_E(num): 
    def mdc(n1,n2):
        rest = 1
        while(n2 != 0):
            rest = n1%n2
            n1 = n2
            n2 = rest
        return n1

    while True:
        e = random.randrange(2,num) 
        if(mdc(num,e) == 1):
            return e

        
'''
Gera um numero primo aleatório
'''
def generate_prime(): # generate the prime number - p e q
    while True: # 2**2048 is the RSA standart keys
        x=random.randrange(1,100) # define the range of the primes
        if(prime(x)==True):
            return x
'''
Função modular entre dois números
'''
def mod(a,b): # mod function
    if(a<b):
        return a
    else:
        c=a%b
        return c

    
    
'''
Cifra um texto
'''
def cipher(words,e,n): # get the words and compute the cipher
    tam = len(words)
    i = 0
    lista = []
    while(i < tam):
        letter = words[i]
        k = ord(letter)
        k = k**e
        d = mod(k,n)
        lista.append(d)
        i += 1
    return lista

'''
Descriptografa um texto criptografado
'''
def descifra(cifra,n,d):
    lista = []
    i = 0
    tamanho = len(cifra)
    # texto=cifra ^ d mod n
    while i < tamanho:
        result = cifra[i]**d
        texto = mod(result,n)
        letra = chr(texto)
        lista.append(letra)
        i += 1
    strng = str('')
    strng1 = strng.join(lista)
    return strng1


'''
Calcula a chave privada
'''
def calculate_private_key(toti,e):
    d = 0
    while(mod(d*e,toti)!=1):
        d += 1
    return d





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



## MAIN
print('Gerando chaves')
if __name__=='__main__':
    #text = input("Insert message: ")
    p = generate_prime() # generates random P
    q = generate_prime() # generates random Q
    n = p*q # compute N
    y = totient(p) # compute the totient of P
    x = totient(q) # compute the totient of Q
    totient_de_N = x*y # compute the totient of N
    e = generate_E(totient_de_N) # generate E
    public_key = (n, e)

    print('Your public key:', public_key)
    #text_cipher = cipher(text,e,n)
    #print('Your encrypted message:', text_cipher)
    d = calculate_private_key(totient_de_N,e)
    print('Your private key is:', d)
    # original_text = descifra(text_cipher,n,d)
#print('your original message:', original_text)


ip, door = ipdoor()
print('Tentando conectar no IP {0} Porta {1}...'.format(ip,door))

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.bind((ip, door))
mysocket.listen(1)
connection, address = mysocket.accept()
print('Conectado com',address)
print('Enviando chave...')
ns = str(n)
ds = str(d)
connection.send(ns.encode('utf-8'))
connection.send(ds.encode('utf-8'))
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
            #connection.send(i.encode('utf-8'))
            text_cipher = cipher(i,e,n)
            ii = str(text_cipher)
            connection.send(ii.encode('utf-8'))
        arq.close()
    except:
        print("Não foi possível abrir o arquivo")
        #print('bug no ciclo : ',bug)
    b = keep()
    if b == 0:
        break
print("fechando conexão...")
connection.close()
mysocket.close()
print('conexões fechadas!')
        
        