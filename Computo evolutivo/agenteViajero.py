# Practic 1
# AGENTE VIAJERO
# Daniel Castillo Torres
# Registro: 4550006
import random
import math
from matplotlib import pyplot as plt

def getAptitudFunction( travel ):
    totalSum = 0
    for i in range( len(travel)-1 ) :
        x2 = travel[i+1][0]
        x1 = travel[i][0]
        y2 = travel[i+1][1]
        y1 = travel[i][1]
        resx = (x2-x1)**2
        resy = (y2-y1)**2
        ressqrt = math.sqrt( resx + resy )
        totalSum += ressqrt
    return totalSum  

def matchMaddness( generation ):
    fighters = []
    for i in range( 5 ):
        randIndex = random.randint(0, itemsByGeneration-1)
        fighters.append( generation[ randIndex ] )
    winner = getBestTravel( fighters )
    return winner

def createNextGeneration( lastGeneration ):
    childs = []
    for i in range( itemsByGeneration ):
        winner = matchMaddness( lastGeneration )
        childs.append( makeChild ( winner['path'] ) )
    return childs

def createNode( path ):
    return {"path":path, "fa":getAptitudFunction( path )}

def makeChild( parent ):
    mitad = len( parent ) / 2
    if( random.randint( 0, 2 ) is not 5 ):
        ini = random.randint( 1, mitad  )
        fin = random.randint( mitad, len( parent ) )
        a, b, c = parent[0:ini], parent[ini:fin], parent[fin:]
        b.reverse()
        child = a + b + c
    else:
        mitad -= 2
        longSubset = random.randint( 1, mitad-1 )
        iniFirst  = random.randint( 1, mitad-longSubset )
        iniSecond = random.randint( mitad, ( len(parent) - 2 ) - longSubset )

        child = parent[:]
        for i in range( longSubset ):
            aux = child[ iniFirst + i ]
            child[ iniFirst + i ] = child[ iniSecond + i ]
            child[ iniSecond + i ] = aux
        del mitad
    return createNode( child )

def getBestTravel( generation ):
    bestTravel = None
    for travel in generation:
        if( bestTravel == None or travel['fa'] < bestTravel['fa'] ):
            bestTravel = travel
    return bestTravel

points = [[1,9],[4,4],[4,9],[1,2],[9,10],[7,7],[9,5],[0,7],[7,6],[3,7],[7,3],[1,6],[1,4],[7,10],[4,2],[9,2],[9,8],[8,9],[5,6],[10,7],[2,9],[2,5],[9,4],[3,1],[6,9],[5,5],[0,0],[9,7],[3,10],[5,8]]

# points = [[3,4],[5,6],[9,7]]
pointsChart = []
currentGeneration = []
numGenerations = 100
itemsByGeneration = 100
# Hacer una matriz de padres de la longitud de points + 1 por 100

for i in range( itemsByGeneration ) :
    parent = random.sample(points, len(points)) 
    currentGeneration.append( createNode( parent ) )

bestsFAs = []
plt.pause(3)
bestGen = None
for i in range( numGenerations ):
    print i+1,".-", getBestTravel( currentGeneration )['fa']
    bestOfThem = getBestTravel( currentGeneration )
    xs = []
    ys = []
    for point in bestOfThem["path"]:
        xs.append(point[0])
        ys.append(point[1])

    bestsFAs.append(bestOfThem["fa"])
    
    plt.figure(figsize=(15, 5))
    plt.subplot(211)
    plt.plot(xs, ys)
    plt.subplot(212)
    plt.plot(bestsFAs)

    plt.show(block=False)
    plt.pause(.1)
    plt.close()

    if bestGen is None or bestGen['fa'] > bestOfThem["fa"]:
        bestGen = bestOfThem

    currentGeneration = createNextGeneration( currentGeneration[:] ) 

xs = []
ys = []
for point in bestGen["path"]:
    xs.append(point[0])
    ys.append(point[1])

plt.title( "The shortest distance found:" +  str( bestGen["fa"] ) )
plt.plot(xs, ys)
plt.scatter(xs, ys, s=120)
plt.show()