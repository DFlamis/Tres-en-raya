import Funciones as fn
print('Bienvenido prro')
PG = input('1. Ver instrucciones\n2. Jugar\nElija un numero: ')
if PG == 1:
    print('Una matriz de la siguiente forma')
    print('   1 | 2 | 3\n   4 | 5 | 6\n   7 | 8 | 9')
    print('Segun el numero que elija es la posision donde aparecera su figura (X o O)')
else:
    PJ = input('Elija la figura\n 1. X\n 2. O\n Ingrese un numero: ')
    while not(PJ.isdigit()):
        PJ = input('Elija la figura\n 1. X\n 2. O\n Ingrese un numero (No una palabra): ')
    while not(0 < int(PJ) < 3):
        PJ = input('Elija la figura\n 1. X\n 2. O\n Ingrese un numero (1 o 2): ')
    print('Nice')
    if int(PJ) == 1:
        A0 = 'X'
        B0 = 'O'
        jug = 0
    else:
        A0 = 'O'
        B0 = 'X'
        jug = 1
    A1 = '-'
    A2 = '-'
    A3 = '-'
    A4 = '-'
    A5 = '-'
    A6 = '-'
    A7 = '-'
    A8 = '-'
    A9 = '-'
    dic = {'1': '-', '2': '-', '3': '-', '4': '-', '5': '-', '6': '-', '7': '-', '8': '-', '9': '-'}
    historial = [] # todos
    HL = [] #solo usuario
    history = set()
    final = ''
    while vk.Raya(A1,A2,A3,A4,A5,A6,A7,A8,A9,B0) == 'False':
        print(f'{A1} | {A2} | {A3}\n{A4} | {A5} | {A6}\n{A7} | {A8} | {A9}')
        elej = input('Escriba el numero: ')
        while not (int(elej) > 0 and int(elej) < 10):
            elej = input('Escriba un numero del 1 al 9: ')
        while elej in historial:
            elej = input(f'Ingrese un numero no usado, {elej} ya esta usado: ')
        historial.append(elej)
        HL.append(int(elej))
        history.add(elej)
        dic[elej] = A0
        #Ver que esta pasando
        print(f'len {len(historial)}')
        print(f'HL {HL}')
        AI = vk.esta(dic,A0,B0,elej,history,HL,historial,jug)
        historial.append(AI)
        dic[AI] = B0
        #Conseguir el valor de cada diccionario
        A1 = dic['1']
        A2 = dic['2']
        A3 = dic['3']
        A4 = dic['4']
        A5 = dic['5']
        A6 = dic['6']
        A7 = dic['7']
        A8 = dic['8']
        A9 = dic['9']
        #Ver que esta pasando x2
        print(f'{historial} len {len(historial)}')
        print(f'AI {AI}')
        print(dic)
        print(f'Validar {vk.Raya(A1,A2,A3,A4,A5,A6,A7,A8,A9,B0)}')
        if vk.Raya(A1,A2,A3,A4,A5,A6,A7,A8,A9,B0) == 'True':
            final = '1'
        elif vk.Raya(A1,A2,A3,A4,A5,A6,A7,A8,A9,B0) == 'Tru':
            final = '2'
    print(f'{A1} | {A2} | {A3}\n{A4} | {A5} | {A6}\n{A7} | {A8} | {A9}')
    if final == '1':
        print('Perdiste')
    elif final == '2':
        print('Empate')
    print('Gracias por jugar xd')