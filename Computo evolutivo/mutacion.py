from __future__ import division
# Practic 2
# Daniel Castillo Torres
# Registro: 4550006
import random
import math
from matplotlib import pyplot as plt

CurrentGeneration = []
NUM_GENERATIONS = 100
ITEMS_BY_GENERATION = 100
CROMOSOMA_SIZE = 3
PORCENTAJE_TORNEO = .05
X = 2
Bests_FA = []
IS_MUTABLE = True
IS_ELITISTA = True

def getAptitudFunction( gen ) :
    fun = ((gen[ 0 ])*(X**2)) + ((gen[ 1 ])*X) + (gen[ 2 ])
    dif = 13 - fun
    return abs( dif )

def matchMaddness( generation ):
    fighters = []
    for i in range( 5 ):
        randIndex = random.randint(0, ITEMS_BY_GENERATION-1)
        fighters.append( generation[ randIndex ] )
    winner = getBestTravel( fighters )
    return winner

def createNextGeneration( lastGeneration ):
    childs = []
    for i in range( ITEMS_BY_GENERATION//2 ):
        parents = []
        for j in range( 2 ) :
            parents.append( matchMaddness( lastGeneration ) )
        childsCreateds = makeChilds ( parents )
        for itChild in childsCreateds :
            childs.append( createNode( itChild ) )
    return childs

def createNode( gen ):
    return {"cromosoma":gen, "fa":getAptitudFunction( gen )}

def makeChilds( parents ):
    alelos = []
    for parent in parents :
        alelosParent = ""
        for j in range( CROMOSOMA_SIZE ):
            alelosParent += createBinaryArrayFromInteger( parent["cromosoma"][ j ] )
        alelos.append( alelosParent )
    # CORTAR LOS ALELOS
    randCut = random.randint( 2, len(alelos[0])-1)
    cromX = alelos[1][0] + alelos[0][1:randCut]
    cromY = alelos[0][randCut:-1] + alelos[1][-1] 
    cromXX= alelos[0][0] + alelos[1][1:randCut]
    cromYY= alelos[1][randCut:-1] + alelos[0][-1] 
    childs = []

    hijo1 = cromX+cromYY
    hijo2 = cromXX+cromY
    if( IS_MUTABLE ):
        randBit = random.randint(0, len(hijo1)-1)
        list1 = list(hijo1)
        list2 = list(hijo2)
        list1[randBit] = '0' if list1[randBit] is '1' else '0'
        list2[randBit] = '0' if list2[randBit] is '1' else '0'

        hijo1 = ''.join(list1)
        hijo2 = ''.join(list2)
    childs.append(createCromosomaFromAlelo(hijo1))
    childs.append(createCromosomaFromAlelo(hijo2))
    
    return childs

def createCromosomaFromAlelo( alelo ) :
    cromosoma = []
    for i in range(CROMOSOMA_SIZE) :
        ini = i*8
        end = (i+1)*8
        n = alelo[ini:end]
        cromosoma.append( int(n,2) )
    return cromosoma

def createBinaryArrayFromInteger( number ) :
    binNum = format(number, '#010b')
    stringReturn = binNum[2:]
    return stringReturn


def getBestTravel( generation ):
    bestTravel = None
    for travel in generation:
        if( bestTravel == None or travel['fa'] < bestTravel['fa'] ):
            bestTravel = travel
    return bestTravel


# Hacer una matriz de padres de la longitud de points + 1 por 100

def createFirstGeneration( ) :
    currentGeneration = []
    for i in range( ITEMS_BY_GENERATION ) :
        cromosoma = []
        for j in range( CROMOSOMA_SIZE ) :
            gen = random.randint(0, 256)
            cromosoma.append( gen )
        currentGeneration.append( createNode( cromosoma ) )
    return currentGeneration


for i in range( NUM_GENERATIONS ):
    CurrentGeneration = createFirstGeneration() if len(CurrentGeneration) == 0 else createNextGeneration( CurrentGeneration[:] )
    bestOfThem = getBestTravel( CurrentGeneration )
    print i+1,".-", bestOfThem['fa']

    Bests_FA.append(bestOfThem["fa"])
    
plt.figure(figsize=(15, 5))
plt.plot(Bests_FA)
plt.show()