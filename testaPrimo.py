# Carlos Felipe Torres de Noronha
while True:
    n = int(input('entre o número : '))
    count = n
    primo = True
    while count > 2:
        count-=1
        if n%count == 0:
            primo = False
    #print('count ',count)
    if primo:
        print(n,' é um número primo')
    else:
        print(n,' não é um número primo')
    if 'i' == input('pressione "i" para interromper !'):
        break