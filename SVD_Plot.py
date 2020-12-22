from PR_Senators import *
from ControversialBills import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_svd(year, U):
    t = pd.DataFrame({"X": U[:, 0], "Y": U[:, 1], "Party": np.array(parties)})
    groups = t.groupby("Party")
    for name, group in groups:
        if name == "PNP":
            col = "b"
        elif name == "PPD":
            col = "r"
        elif name == "PIP":
            col = "g"
        elif name == "indep.":
            col = "k"
        plt.plot(group["X"], group["Y"], col, marker="o", linestyle="", label=name, color=col)
    plt.legend()
    plt.title("SVD Analysis " + str(year))
    plt.show()

def plot_pc(year, U_S): # U_S is a list of the form [U, S]
    A = U_S[0] @ np.diag(U_S[1])
    t = pd.DataFrame({"X": A[:, 0], "Y": A[:, 1], "Party": np.array(parties)})
    groups = t.groupby("Party")
    for name, group in groups:
        if name == "PNP":
            col = "b"
        elif name == "PPD":
            col = "r"
        elif name == "PIP":
            col = "g"
        elif name == "indep.":
            col = "k"
        plt.plot(group["X"], group["Y"], col, marker="o", linestyle="", label=name, color=col)
    plt.legend()
    plt.title("Principal Component (Scaled SVD) Analysis " + str(year))
    plt.show()


myData = read_txt(1, 16)

plot_err("2017-2020", myData)
plt.savefig("2017-2020 error.png")
plt.close()

plot_svd("2017-2020", u_sig(myData)[0])
plt.savefig("2017-2020 SVD.png")
plt.close()

plot_pc("2017-2020", u_sig(myData))
plt.savefig("2017-2020 PCA.png")
plt.close()


for i in range(4):

    myData = read_txt(4 * i + 1, 4 * i + 4)

    plot_err(i + 2017, myData)
    plt.savefig(str(i + 2017) + " error.png")
    plt.close()

    plot_svd(i + 2017, u_sig(myData)[0])
    plt.savefig(str(i + 2017) + " SVD.png")
    plt.close()

    plot_pc(i + 2017, u_sig(myData))
    plt.savefig(str(i + 2017) + " PCA.png")
    plt.close()

myData = cont_bills(1, 16)

plot_err("2017-2020 *", myData)
plt.savefig("2017-2020 controversial error.png")
plt.close()


plot_svd("2017-2020 *", u_sig(myData)[0])
plt.savefig("2017-2020 controversial SVD.png")
plt.close()

plot_pc("2017-2020 *", u_sig(myData))
plt.savefig("2017-2020 controversial PCA.png")
plt.close()

myData = not_cont_bills(1, 16)

plot_err("2017-2020 **", myData)
plt.savefig("2017-2020 not controversial error.png")
plt.close()

plot_svd("2017-2020 **", u_sig(myData)[0])
plt.savefig("2017-2020 not controversial SVD.png")
plt.close()

plot_pc("2017-2020 **", u_sig(myData))
plt.savefig("2017-2020 not controversial PCA.png")
plt.close()

for i in range(4):
    myData = cont_bills(4 * i + 1, 4 * i + 4)

    plot_err(str(i + 2017) + "*", myData)
    plt.savefig(str(i + 2017) + " controversial error.png")
    plt.close()

    plot_svd(str(i + 2017) + "*", u_sig(myData)[0])
    plt.savefig(str(i + 2017) + " controversial SVD.png")
    plt.close()

    plot_pc(str(i + 2017) + "*", u_sig(myData))
    plt.savefig(str(i + 2017) + " controversial PCA.png")
    plt.close()

    myData = not_cont_bills(4 * i + 1, 4 * i + 4)

    plot_err(str(i + 2017) + "**", myData)
    plt.savefig(str(i + 2017) + " not controversial error.png")
    plt.close()

    plot_svd(str(i + 2017) + "**", u_sig(myData)[0])
    plt.savefig(str(i + 2017) + " not controversial SVD.png")
    plt.close()

    plot_pc(str(i + 2017) + "**", u_sig(myData))
    plt.savefig(str(i + 2017) + " not controversial PCA.png")
    plt.close()
