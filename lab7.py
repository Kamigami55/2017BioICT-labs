from __future__ import print_function

print("Please enter n: ", end='')
n = input()

def printDiamond(n):
    for i in range(n):
        print(" "*(n-i-1), end='')
        print("*"*(i*2+1))

    for i in range(n-2, -1, -1):
        print(" "*(n-i-1), end='')
        print("*"*(i*2+1))


printDiamond(n)
