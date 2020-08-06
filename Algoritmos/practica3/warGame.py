# This Python file uses the following encoding: utf-8
# Análisis y diseño de algoritmos
# Daniel Castillo Torres
# Práctica 3 - War game

import sys

ListaEnemigos = []
tree = []

def main():
    parsedFile = readFile("input2.txt")

    for line in parsedFile:
        result = runOperation(line[0], line[1], line[2])
        if result != None:
            print( result )

def setFriends(x,y): 

    global tree

    tree1 = findTree(x)
    tree2 = findTree(y)

    if tree1 != -1 and (tree1 == tree2):
        return
    if tree1 == -1 and tree2 ==  -1:
        tree.append([x,y])
        return
    if tree1 == -1:
        tree[tree2].append(x)
        return
    if tree2 == -1:
        tree[tree1].append(y)
        return

    enemyTree1 = searchEnemy(tree1)
    enemyTree2 = searchEnemy(tree2)

    if enemyTree1 == -1 and (enemyTree1 == enemyTree2):
        tree[tree1].extend( tree[tree2] )
        tree[tree2] = []
        return


    if enemyTree1 != -1 and (enemyTree1 == enemyTree2):
        return -1

    joinT(tree1, enemyTree1, tree2, enemyTree2, True)

def joinT(arbola1, arbole1, arbola2, arbole2, areFriends ):
    if areFriends is True:
        if arbole1 == -1 or arbole2 == -1:
            sourceTree = arbola1 if arbole1 == -1 else arbola2
            targetTree = arbola2 if arbole1 == -1 else arbola1
            for item in tree[sourceTree]:
                tree[targetTree].append( item )
            tree.pop( sourceTree )
        else:
            for item in tree[arbola2]:
                tree[arbola1].append( item )
            tree.pop( arbola2 )
            for itemE1 in ListaEnemigos[arbole2] :
                if itemE1 is not arbola2:
                    for itemE2 in ListaEnemigos[arbole1]:
                        if itemE2 is not arbola1 :
                            for moveEnemy in tree[itemE1]:
                                tree[itemE2].append( moveEnemy )
                            
                            break
                    tree.pop( itemE1 )
                    ListaEnemigos.pop( arbole2 )
                    break
    else:
        for itemE1 in ListaEnemigos[arbole2] :
            if itemE1 is not arbola2:
                for itemA1 in tree[arbola1] :
                    tree[itemE1].append( itemA1 )
                tree.pop( arbola1 )
                break
        for itemE2 in ListaEnemigos[arbole1] :
            if itemE2 is not arbola1:
                for itemA2 in tree[itemE2] :
                    tree[arbola2].append( itemA2 )
                tree.pop( itemE2 )
                break
        ListaEnemigos.pop( arbole1 )


def setEnemies(x,y): 

    global ListaEnemigos
    global tree

    tree1 = findTree(x)
    tree2 = findTree(y)


    if tree1 != -1 and (tree1 == tree2):
        return -1

    if tree1 == -1 and tree2 == -1:
        tree.append([x])
        tree.append([y])
        ListaEnemigos.append([len(tree)-1, len(tree)-2])
        return

    enemyTree1 = searchEnemy(tree1)
    enemyTree2 = searchEnemy(tree2)

    if tree1 == -1:
        if enemyTree2 == -1:
            tree.append([x])
            ListaEnemigos.append([tree2, len(tree)-1])
        else:
            enemiX, enemiY = ListaEnemigos[enemyTree2]
            if tree2 == enemiX:
                tree[enemiY].append(x)
            else:
                tree[enemiX].append(x)
        return

    if tree2 == -1:
        if enemyTree1 == -1:
            tree.append([y])
            ListaEnemigos.append([tree1, len(tree)-1])
        else:
            enemiA, enemiB = ListaEnemigos[enemyTree1]
            if tree1 == enemiA:
                tree[enemiB].append(y)
            else:
                tree[enemiA].append(y)
        return

    if enemyTree1 == -1 and enemyTree2 == -1:
        ListaEnemigos.append([tree1, tree2])
        return

    joinT(tree1, enemyTree1, tree2, enemyTree2, False)


def areFriends(x,y):

    tree1 = findTree(x)
    if y in tree[tree1]:
        return 1
    else:
        return 0

def areEnemies(x,y):

    tree1 = findTree(x)
    tree2 = findTree(y)
    if tree1 == -1 or tree2 == -1:
        return 0
    elif tree1 == tree2:
       return 0

    enemyTree1 = searchEnemy(tree1)
    enemyTree2 = searchEnemy(tree2)
    if enemyTree1 == -1 or enemyTree2 == -1 or enemyTree1 != enemyTree2:
        return 0
    else:
        return 1


def findTree(x):  
    for i in range(len(tree)):
        if x in tree[i]:
            return i
    return -1

def searchEnemy(tree):  
    for i in range(len(ListaEnemigos)):
        if tree in ListaEnemigos[i]:
            return i
    return -1

def readFile(filename):
    n = 0
    operations = []
    with open(filename,'r') as f:
        n = f.readline()
        n = int(n.replace('\n',''))
        if n <= 0 or n > 10000:
            raise ValueError("El valor debe estar entre 0 y 10,000")
        for line in f:
            line = line.replace('\n','')
            datos = line.split(' ')
            c = int(datos[0])
            x = int(datos[1])
            y = int(datos[2])
            if c == 0 and x == 0 and y == 0:
                break

            operations.append([c, x, y])

    return operations

def runOperation(c, x, y):
    if c == 1:
        return setFriends(x, y)
    elif c == 2:
        return setEnemies(x, y)
    elif c == 3:
        return areFriends(x, y)
    elif c == 4:
        return areEnemies(x, y)
    else:
        raise ValueError( "La función no es válida" )

if __name__ == "__main__":
    main()