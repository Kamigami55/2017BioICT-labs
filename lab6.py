from __future__ import print_function

print("Please enter n: ", end='')
n = input()

def printTriangle(n):
    for i in range(n+1):
        print(" "*(n-i), end='')
        print("*"*i)


printTriangle(n)
