# This Python file uses the following encoding: utf-8
#!/usr/bin/python3

import sys
import numpy

DEBUG=True
ListaEnemigos = []
Arboles = []

def setFriends(x,y): #Mismo país hacer amigos

    global Arboles

    arbola1 = searchArbol(x)
    arbola2 = searchArbol(y)

    # if they are in the same group, do nothing
    if arbola1 != -1 and (arbola1 == arbola2):
        return
    # if none of them are in any group, then create new group
    if arbola1 == -1 and arbola2 ==  -1:
        Arboles.append([x,y])
        return
    # if x is not part of a group, then add it to the same group as y
    if arbola1 == -1:
        Arboles[arbola2].append(x)
        return
    # if y is not part of a group, then add it to the same group as x
    if arbola2 == -1:
        Arboles[arbola1].append(y)
        return

    arbole1 = searchEnemy(arbola1)
    arbole2 = searchEnemy(arbola2)

    if arbole1 == -1 and (arbole1 == arbole2):
        Arboles[arbola1].extend( Arboles[arbola2] )
        Arbol[arbola2] = []
        return


    if arbole1 != -1 and (arbole1 == arbole2):
        return -1

    unirArboles(arbola1, arbole1, arbola2, arbole2, True)

def unirArboles(arbola1, arbole1, arbola2, arbole2, areFriends ):
    if areFriends is True:
        if arbole1 == -1 or arbole2 == -1:
            sourceTree = arbola1 if arbole1 == -1 else arbola2
            targetTree = arbola2 if arbole1 == -1 else arbola1
            for item in Arboles[sourceTree]:
                Arboles[targetTree].append( item )
            Arboles.pop( sourceTree )
        else:
            for item in Arboles[arbola2]:
                Arboles[arbola1].append( item )
            Arboles.pop( arbola2 )
            for itemE1 in ListaEnemigos[arbole2] :
                if itemE1 is not arbola2:
                    for itemE2 in ListaEnemigos[arbole1]:
                        if itemE2 is not arbola1 :
                            for moveEnemy in Arboles[itemE1]:
                                Arboles[itemE2].append( moveEnemy )
                            
                            break
                    Arboles.pop( itemE1 )
                    ListaEnemigos.pop( arbole2 )
                    break
    else:
        for itemE1 in ListaEnemigos[arbole2] :
            if itemE1 is not arbola2:
                for itemA1 in Arboles[arbola1] :
                    Arboles[itemE1].append( itemA1 )
                Arboles.pop( arbola1 )
                break
        for itemE2 in ListaEnemigos[arbole1] :
            if itemE2 is not arbola1:
                for itemA2 in Arboles[itemE2] :
                    Arboles[arbola2].append( itemA2 )
                Arboles.pop( itemE2 )
                break
        ListaEnemigos.pop( arbole1 )

def setEnemies(x,y):  #Paises diferentes hacer enemigos

    global ListaEnemigos
    global Arboles

    arbola1 = searchArbol(x)
    arbola2 = searchArbol(y)


    if arbola1 != -1 and (arbola1 == arbola2):
        return -1

    if arbola1 == -1 and arbola2 == -1:
        Arboles.append([x])
        Arboles.append([y])
        ListaEnemigos.append([len(Arboles)-1, len(Arboles)-2])
        return

    arbole1 = searchEnemy(arbola1)
    arbole2 = searchEnemy(arbola2)

    if arbola1 == -1:
        if arbole2 == -1:
            Arboles.append([x])
            ListaEnemigos.append([arbola2, len(Arboles)-1])
        else:
            enemiX, enemiY = ListaEnemigos[arbole2]
            if arbola2 == enemiX:
                Arboles[enemiY].append(x)
            else:
                Arboles[enemiX].append(x)
        return

    if arbola2 == -1:
        if arbole1 == -1:
            Arboles.append([y])
            ListaEnemigos.append([arbola1, len(Arboles)-1])
        else:
            enemiA, enemiB = ListaEnemigos[arbole1]
            if arbola1 == enemiA:
                Arboles[enemiB].append(y)
            else:
                Arboles[enemiA].append(y)
        return

    if arbole1 == -1 and arbole2 == -1:
        ListaEnemigos.append([arbola1, arbola2])
        return

    unirArboles(arbola1, arbole1, arbola2, arbole2, False)


def areFriends(x,y): #Pregunta si son amigos

    arbola1 = searchArbol(x)
    if y in Arboles[arbola1]:
        return True
    else:
        return False

def areEnemies(x,y):  #Preguntar si son enemigos

    arbola1 = searchArbol(x)
    arbola2 = searchArbol(y)
    if arbola1 == -1 or arbola2 == -1:
        return False
    elif arbola1 == arbola2:
       return False

    arbole1 = searchEnemy(arbola1)
    arbole2 = searchEnemy(arbola2)
    if arbole1 == -1 or arbole2 == -1 or arbole1 != arbole2:
        return False
    else:
        return True


def searchArbol(x):  #Enemigos -1
    for i in range(len(Arboles)):
        if x in Arboles[i]:
            return i
    return -1

def searchEnemy(arbol):  #Enemigos -1
    for i in range(len(ListaEnemigos)):
        if arbol in ListaEnemigos[i]:
            return i
    return -1

def numentero(n):
    if n <= 0 or n > 10000:
        raise ValueError("n is between 1 - 10000")

def validatePeople(n, p1, p2):
    if p1 < 0 or p1 >= n:
        raise ValueError("parameter {0} should be less than {1}".format(p1, n))
    if p2 < 0 or p1 >= n:
        raise ValueError("parameter {0} should be less than {1} ".format(p2, n))

def validateOperation(c):
    if c <= 0 or c >= 5:
        raise ValueError("Invalid operation {0}, c is between 1 - 4".format(c))

def parseDataFromFile(filename):
    n = 0
    operations = []
    print("Reading data from file {0}".format(filename))
    with open(filename,'r') as f:
        n = f.readline()
        n = int(n.replace('\n',''))
        numentero(n)
        for line in f:
            line = line.replace('\n','')
            datos = line.split(' ')
            if len(datos) != 3:
                raise ValueError("Faltan argumentos: operacion personaN personaM")
            c = int(datos[0])
            p1 = int(datos[1])
            p2 = int(datos[2])
            if c == 0 and p1 == 0 and p2 == 0:
                break

            validateOperation( c )
            validatePeople(n, p1, p2)
            operations.append([c, p1, p2])

    return operations

def resultados(op, person1, person2):
    if op == 1:
        func_name="setFriends"
        res = setFriends(person1, person2)
    if op == 2:
        func_name="setEnemies"
        res = setEnemies(person1, person2)
    if op == 3:
        func_name="areFriends"
        res = areFriends(person1, person2)
    if op == 4:
        func_name="areEnemies"
        res = areEnemies(person1, person2)

    if DEBUG==True:
        print("=========================================")
        print("{0}({1},{2}) ".format(func_name, person1, person2))
        print("output = {0}".format(res))
        print("Arboles")
        print(Arboles)
        print("Enemies")
        print(ListaEnemigos)
    return res



def main():
    global DEBUG

    if len(sys.argv) == 2:
        testFile = sys.argv[1]
    elif len(sys.argv) == 3:
        testFile = sys.argv[1]
        if sys.argv[2] == '-D':
            DEBUG=True
    else:
        testFile = "input2.txt"

    output = []
    operations = parseDataFromFile(testFile)

    if DEBUG==True:
        for op in operations:
            print(op)

    for op in operations:
        res = resultados(op[0], op[1], op[2])
        if res == True:
            res = 1
        if res == False:
            res = 0
        if res != None:
            output.append(res)
    print("=========================================")
    print("output: {0}".format(output))

if __name__ == "__main__":
    main()