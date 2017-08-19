from __future__ import print_function
import names
import random

def generateRandomScores(n):
    scores = {}
    for i in range(n):
        scores[names.get_first_name()] = random.randint(0, 100)
    return scores


print("Please enter n: ", end='')
n = input()

scores = generateRandomScores(n)

print("Name          | Score")
print("========================")

for (key, val) in scores.iteritems():
    print(key.ljust(13) + " | " + str(val).rjust(3))

print("\n-------------------------------------------")

print("Name          | Score")
print("========================")

for idx, t in enumerate(sorted(scores.items(), key=lambda x: x[1], reverse=True)):
    if idx > 2:
        break
    print(t[0].ljust(13) + " | " + str(t[1]).rjust(3))
    
