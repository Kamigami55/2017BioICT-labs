from __future__ import print_function
import numpy as np
import random

def matrixMult(a, b):
    a = 1

def generateMatrix(n, m):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(random.randint(0, 10))
    return matrix

def printMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in n:
        print(matrix)



print("Please enter n: ", end='')
n = input()
print("Please enter m: ", end='')
m = input()

a = generateMatrix(n, m)
b = generateMatrix(m, n)
print("Matrix A is:")
print(np.matrix(a))
print("\nMatrix B is:")
print(np.matrix(b))

result = np.dot(a, b)
print("\nResult is:")
print(np.matrix(result))

largest = 0
largestN = 0
largestM = 0
for i in range(n):
    for j in range(n):
        if result[i][j] > largest:
            largest = result[i][j]
            largestN = i+1
            largestM = j+1

print("\nLargest num: %d [%d][%d]" % (largest, largestN, largestM))
