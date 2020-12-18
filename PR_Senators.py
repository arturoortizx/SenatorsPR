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
        senators = senators + [[[previous.removeprefix("Votante : ")]]]
    previous = line
f.close()

# adding political party to each senator:

for i in range(len(senators)):
    if i in [0, 2, 3, 6, 7, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 28, 29]:
        senators[i][0] = senators[i][0] + ["PNP"]
    elif i in [1, 5, 8, 11, 17, 25, 26,]:
        senators[i][0] = senators[i][0] + ["PPD"]
    elif i == 4:
        senators[i][0] = senators[i][0] + ["PIP"]
    elif i == 27:
        senators[i][0] = senators[i][0] + ["indep."]

senators_ = senators
print(senators_)


parties = []
for i in range(len(senators)):
    parties = parties + [senators[i][0][1]]

votes_per_sen = []

# records each senators vote for each bill
def read_txt(x, y):
    senators = senators_
    for file in range(x, y):
        for n in range(len(senators)):
            bill_num = []
            passed_senator = False
            f = open("PRSenate" + str(file) + ".txt", "r")
            sen_name = senators[n][0][0]
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

    for m in range(len(senators)):
        df = df.rename(index={m : senators[m][0][0]})

    print(df)


    print(np.zeros(np.shape(myData)))

    return myData


def plot_err(title, d):
    error = np.zeros([np.linalg.matrix_rank(d), 1])
    for k in range(1, np.linalg.matrix_rank(d)):
        [U, S, V] = SVD.rsvd(d, k, 5, 1)
        Ak = np.zeros((30, np.linalg.matrix_rank(d)), int)
        for i in range(k):
            Ak = U @ np.diag(S) @ V
        error[k - 1] = np.linalg.norm(d - Ak) / np.linalg.norm(d)

    plt.plot(error)
    plt.title(title)
    plt.show()

def u_ret(d):
    r = np.linalg.matrix_rank(d)
    [U, S, V] = SVD.rsvd(r, r, 5, 1)[0]
    return U

