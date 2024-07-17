import numpy as np


def V_i(x):
    mu = np.array([-1, 1])
    rtn = np.exp(-((x - mu) ** 2))
    print(rtn)
    return rtn


def xi(w):
    w_1 = w[0]
    w_2 = w[1]
    xi = (-w_1 + w_2) / (w_1 + w_2)
    return xi

def F_payoff(w):
    return -V_i(xi(w))

if __name__ == "__main__":
    x = np.array([1, 0])
    print(F_payoff(x))
