import numpy as np
import pandas as pd
import RandomSVD as SVD
import matplotlib.pyplot as plt

# Plan:
# check for string "Fecha", which appears right after each senator's name
# For each senator make a row
# For each row check each line until we find a line that is all numbers.
# and then associate the first non number line with that to that column number
# Then give each type of vote a number
# -1 for en contra, 1 for a favor, 0 otherwise

def vote_to_num(text):
    """ Converts the type of vote to 1, -1, or 0"""
    if text == "A favor":
        return 1
    if text == "En contra":
        return -1
    return 0

# removes blank lines from the txt file
f = open("PRSenate1.txt", "r")
lines = f.readlines()
f.close()

lines = filter(lambda x: not x.isspace(), lines)

f = open("noblanks.txt", "w")
f.write("".join(lines))
f.close()

# Makes a list of senators
f = open("noblanks.txt", "r")
senators = []
previous = ""
for line in f:
    line = line.removesuffix("\n")
    if "Fecha" in line:
        senators = senators + [[previous.removeprefix("Votante : ")]]
    previous = line
senators_ = senators
print(senators_)
f.close()

votes_per_sen = []

# records each senators vote for each bill
for file in range(16):
    for n in range(len(senators)):
        bill_num = []
        passed_senator = False
        f = open("PRSenate" + str(file + 1) + ".txt", "r")
        sen_name = senators[n][0]
        for pos, l in enumerate(f):
            l = l.replace("\r", "").replace("\n", "")
            if "Votante" in l and passed_senator:
                break

            if sen_name in l:
                passed_senator = True
            if passed_senator:
                if l.isnumeric():
                    bill_num.append(l)
            if ("Ausente" in l or "A favor" in l or "En contra" in l or "Abstenido" in l) and passed_senator and bill_num:
                senators[n].append([bill_num.pop(0), vote_to_num(l)])
        f.close()

print(senators)
# Figuring out the numbers of the distinct bill numbers
billNums = dict()
billCount = 0

for L in senators:
    for i in range(1, len(L)):
        Li = L[i][0]
        if Li not in billNums:
            billNums[Li] = billCount
            billCount = billCount + 1

# Creating the matrix/table
myData = np.zeros([30, len(billNums)])

for i in range(30):
    Li = senators[i]
    for j in range(1, len(Li)):
        Lj = Li[j]
        jdx = billNums[Lj[0]]
        myData[i, jdx] = Lj[1]


df = pd.DataFrame(myData)
for n in range(len(list(billNums.keys()))):
    df = df.rename(columns={n : list(billNums.keys())[n]})

for m in range(len(senators_)):
    df = df.rename(index={m : senators_[m][0]})

print(df)

[U, S, V] = SVD.rsvd(myData, 30, 1, 5)
print(np.zeros(np.shape(myData)))
error = np.zeros([np.linalg.matrix_rank(myData), 1])

A = np.zeros((30, np.linalg.matrix_rank(myData)), int)
for i in range(np.linalg.matrix_rank(myData)):
    A = A + S[i, i] * (U[:, i].dot(V[:, i]))

for k in range(np.linalg.matrix_rank(myData)):
    Ak = np.zeros((30, np.linalg.matrix_rank(myData)), int)
    for i in range(k):
        Ak = Ak + S[i, i] * (U[:, i].dot(V[:, i]))
    error[k] = np.linalg.norm(A - Ak, 2)

print(plt.plot(error))

# Making the plot
# plt.scatter(U1, U2)
# plt.show()
# Or
#plt.savefig("svdplot.png")
#plt.close()
#U = svd[0]
#plt.scatter(U[:,0], U[:,1])

# Figuring out rank
# np.linalg.norm(myData - myData_k, 2)
# Uk @ Sk @ Vk
# np.linalg.norm(myData - myData_k, 2) / np.linalg.norm(myData, 2)

# plt.scatter(U1, U2) instead of plot
# Color code the plots
