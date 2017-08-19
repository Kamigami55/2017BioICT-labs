from __future__ import print_function
import operator as op

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

print("Please enter n: ", end='')
n = input()

for i in range(n): # rows
    print("   "*(n-i-1), end='')
    for j in range(i+1):
        print(str(ncr(i, j)).center(6), end='')
    print('')
