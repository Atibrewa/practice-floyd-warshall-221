import random
import sys
import csv
import time

def FloydWarshall(W):
    """
    W is an n by n 2D array, adjacency matrix for a graph w n vertices
    """
    D = [[0 for _ in range(len(W))] for _ in range(len(W))] #keeps track of cost
    Path = [[0 for _ in range(len(W))] for _ in range(len(W))] #keeps track of pred
    n = len(W)
    for i in range(n):
        for j in range(n):
            D[i][j] = W[i][j]
            if W[i][j] == sys.maxsize:
                Path[i][j] = -1
            else:
                Path[i][j] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (D[i][j] > (D[i][k] + D[k][j])):
                    D[i][j] = D[i][k] + D[k][j]
                    Path[i][j] = Path[k][j]
    return D, Path  
                 

def pathReconstruct(Path, start, end):
    """
    Reconstructs the path from the start to end nodes in the graph based on the matrix Path
    """
    p = []
    p.append(end)
    while end != start:
        end = Path[start][end]
        p.append(end)
    p.reverse()
    return p


def readCSV(file):
    inputArr = list(csv.reader(open(file)))
    NewArray = [[0 for _ in range(len(inputArr))] for _ in range(len(inputArr))] 
    j = 0
    for i in inputArr:
        NewArray[j].append(i)
        j += 1
    return NewArray


def printMatrix(M):
    """
    M is a n by n 2D matrix that gets printed in a pretty looking format!
    """
    for i in range(len(M)) :
        for j in range (len(M)):
            print (M[i][j], end='   ')
        print ()
    print ()


def generateMatrix(n):
    """
    Generates a matrix of size n by n with inputts ranging from 1 to maxsize
    """
    M = [[0 for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            M[a][b] = random.randint(1, 9)
    return M


# test matrix!
test1 = [[6, 8, 5, 2], 
        [3, 9, sys.maxsize, sys.maxsize], 
        [sys.maxsize, 2, 2, sys.maxsize], 
        [7, sys.maxsize, 1, 7]] 


while True:
    # (1) taking user's choice for matrix!
    choice = int(input("(1) test matrix,\n(2) randomly generated matrix"))
    if choice == 2 :
        m = int(input("Enter size of random matrix!"))
        arr = generateMatrix(m)
        print ("The starting Adjacency Matrix is: ")
        printMatrix(arr)
    else :
        arr = test1

    starttime1 = time.time()
    # (2) running Warshall's and printing the output
    D, Path = FloydWarshall(arr)
    endtime1 = time.time()
    print('time =' , endtime1 - starttime1)
    print ("D is: ")
    printMatrix(D)
    print ("Path is: ")
    printMatrix(Path)

    # (3) taking input of start and end
    start = int(input("Index of start node: "))
    end = int(input("Index of end node: "))

    # (4) printing the reconstructed shortest path and its cost
    starttime = time.time()
    p = pathReconstruct(Path, start, end)
    endtime = time.time()
    print('path reconstruct time =' , endtime - starttime)
    print ("The path from {0} to {1} is: ".format(str(start), str(end)))
    print ("\t", p)
    print ("The cost of this path is: ", D[start][end])

    # Restarts/Ends the loop
    ans = input("Another Matrix? Y/N")
    if ans.lower() == 'y':
        continue
    else:
        break