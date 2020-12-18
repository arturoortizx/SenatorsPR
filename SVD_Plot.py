from PR_Senators import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_all(title, U):
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
    plt.title(title)
    plt.show()

myData = read_txt(1, 16)
plot_err("All Bills 2017-2020", myData)
plot_all("All Bills 2017-2020", u_ret(myData))

myData = read_txt(1, 4)
plot_err("All Bills 2017", myData)
plot_all("All Bills 2017", u_ret(myData))

myData = read_txt(5, 8)
plot_err("All Bills 2018", myData)
plot_all("All Bills 2018", u_ret(myData))

myData = read_txt(9, 12)
plot_err("All Bills 2019", myData)
plot_all("All Bills 2019", u_ret(myData))

myData = read_txt(13, 16)
plot_err("All Bills 2020", myData)
plot_all("All Bills 2020", u_ret(myData))
