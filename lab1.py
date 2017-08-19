from __future__ import print_function
import random

def generateRandomList(n):
    array = []
    for i in range(n):
        array.append(random.randint(1,99))
    return array

print("Please enter n: ", end='')
n = input()

array = generateRandomList(n)

print("Generate array: ", end='')
print(array)

sum = 0

for num in array:
    if num % 2 == 0:
        sum = sum + 1

print("Even number count: " + str(sum))
