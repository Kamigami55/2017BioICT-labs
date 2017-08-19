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
print("Please enter m: ", end='')
m = input()

math_scores = generateRandomScores(n)
eng_scores = generateRandomScores(n)

print("[ M A T H ]")
print("Name          | Score")
print("========================")
for (key, val) in math_scores.iteritems():
    print(key.ljust(13) + " | " + str(val).rjust(3))
print('')
highest = sorted(math_scores.items(), key=lambda x: x[1], reverse=True)[0]
print("Highest: %s %s" % (highest[0], highest[1]))
print("\n-------------------------------------------")

print("[ E N G L I S H ]")
print("Name          | Score")
print("========================")
for (key, val) in eng_scores.iteritems():
    print(key.ljust(13) + " | " + str(val).rjust(3))
print('')
highest = sorted(eng_scores.items(), key=lambda x: x[1], reverse=True)[0]
print("Highest: %s %s" % (highest[0], highest[1]))
