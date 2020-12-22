from PR_Senators import *

def count_ones(col):
    ones = 0
    for i in col:
        if i == 1:
            ones = ones + 1
    return ones

def cont_bills(x, y):
    myData = read_txt(x, y)

    cont = 0
    for i in range(np.shape(myData)[1]):
        if count_ones(myData[:, i]) in range(5, 25):
           cont = cont + 1

    A = np.zeros([30, cont])
    j = 0
    for i in range(np.shape(myData)[1]):
        if count_ones(myData[:, i]) in range(5, 25):
            A[:, j] = myData[:, i]
            j = j + 1

    return A

def not_cont_bills(x, y):
    myData = read_txt(x, y)

    cont = 0
    for i in range(np.shape(myData)[1]):
        if count_ones(myData[:, i]) not in range(5, 25):
           cont = cont + 1

    A = np.zeros([30, cont])
    print(cont)
    j = 0
    for i in range(np.shape(myData)[1]):
        if count_ones(myData[:, i]) not in range(5, 25):
            A[:, j] = myData[:, i]
            j = j + 1

    return A


