from __future__ import print_function
import names
import random

def generateRandomScores(n):
    scores = {}
    for i in range(n):
        scores[names.get_first_name()] = random.randint(0, 100)
    return scores

def generateEngScores(math):
    eng_scores = {}
    for (key, val) in math.iteritems():
        eng_scores[key] = random.randint(0, 100)
    return eng_scores


def generateSum(math, eng):
    sum_scores = {}
    for (key, val) in math.iteritems():
        sum_scores[key] = math[key] + eng[key]
    return sum_scores

#print("Please enter n: ", end='')
n = 7
#print("Please enter m: ", end='')
#m = 6

math_scores = generateRandomScores(n)
eng_scores = generateEngScores(math_scores)

print("[ M A T H ]")
print("Name          | Score")
print("========================")
for (key, val) in math_scores.iteritems():
    print(key.ljust(13) + " | " + str(val).rjust(3))
print('')

print("[ E N G L I S H ]")
print("Name          | Score")
print("========================")
for (key, val) in eng_scores.iteritems():
    print(key.ljust(13) + " | " + str(val).rjust(3))
print('')


sum_scores = generateSum(math_scores, eng_scores)

for idx, tup in enumerate(sorted(sum_scores.items(), key=lambda x: x[1], reverse=True)):
    if idx > 2:
        break
    print("%s %d (%d + %d)" % (tup[0], tup[1], math_scores[tup[0]], eng_scores[tup[0]]))
