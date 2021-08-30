import random as rn

#Validar victoria o empate
def Raya(A1,A2,A3,A4,A5,A6,A7,A8,A9,A0):
    #A0 = X
    #A1 = -
    L1 = []
    for n in (A1,A2,A3,A4,A5,A6,A7,A8,A9):
        if n != '-':
            L1.append(0)
        else:
            L1.append(1)
    if sum(L1) >= 1:
        #Horizontales
        if A1 == A0 and A2 == A0 and A3 == A0:
            return 'True'
        elif A4 == A0 and A5 == A0 and A6 == A0:
            return 'True'
        elif A7 == A0 and A8 == A0 and A9 == A0:
            return 'True'
        #Verticales
        elif A1 == A0 and A4 == A0 and A7 == A0:
            return 'True'
        elif A2 == A0 and A5 == A0 and A8 == A0:
            return 'True'
        elif A3 == A0 and A6 == A0 and A9 == A0:
            return 'True'
        #Diagonales
        elif A1 == A0 and A5 == A0 and A9 == A0:
            return 'True'
        elif A3 == A0 and A5 == A0 and A7 == A0:
            return 'True'
        #Falso
        else:
            return 'False'
    else:
        return 'Tru'

#Retorna el valor de la AI
def esta(dic,A0,B0,elej,history,HL,historial,jug):
    turn = len(historial)
    corner = {'1','3','7','9'}
    side = {'2','4','6','8'}
    val = len(history & corner)
    HL = sorted(HL)
    if turn == 1 + jug:
        if val == 1:
            return '5'
        #side    
        else:
            opera = 10 - int(elej)
            AI = rn.choice(list(side - {str(opera)} - {elej}))
            return AI

    elif turn == 3: #Especial
        if val == 2:
            HL.sort()
            operacion = HL[1] - HL [0]
            if operacion == 2:
                return str(HL[1] - 1)
            elif operacion == 6:
                return str(HL[1] - 3)
            else:
                return rn.choice(list(side))    
        else:
            if historial[0] == '2':
                opera = int(historial[1]) - 3
                if str(opera) not in historial[2]:
                    return str(opera)
                else:
                    opera = 7 - int(historial[1])
                    return str(opera)

    elif turn == 5 + jug:
        if mesalioxd(historial) != int(elej):
            return str(mesalioxd(historial))
        elif mesalioxd(historial) == int(elej):
            AI = rn.choice(list(side - set(historial)))
            return AI
            
    elif turn == 7 + jug:
        if elej not in list(side):
            return list(side - set(historial))[0]
        elif elej in list(side):
            return rn.choice(list(corner - set(historial)))

#No tengo ni pta idea de que hace esto pero es importante        
def mesalioxd(listar):
    lista = listar[:]
    if '5' in lista:
        lista.remove('5')
    lista.pop()
    lista.sort()
    operacion = int(lista[0]) + int(lista[2]) + 10 - (int(lista[1])*3)
    print(f'-> operacion {operacion}')
    return operacion
    