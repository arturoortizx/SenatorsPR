import numpy as np
import pandas as pd
import RansomSVD as SVD
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
f = open("output.txt", "r")
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
for n in range(len(senators)):
    bill_num = []
    passed_senator = False
    f = open("noblanks.txt", "r")
    for pos, l in enumerate(f):
        l = l.removesuffix("\n")
        if senators[n - 1][0] in l:
            senator = senators[n]
            passed_senator = True
            t = 0
        if passed_senator:
            if l.isnumeric():
                bill_num = bill_num + [l, pos]
                t = t + 1
        if pos - 29 in bill_num:
            bill = bill_num[bill_num.index(pos - 29) - 1]
            vote = l
            senators[n] = senators[n] + [[bill, vote_to_num(l)]]

    f.close()

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

svd = SVD.rsvd(myData, 30, 1, 5)

print(svd)
