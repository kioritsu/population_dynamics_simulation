import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from dynamics import bnn, replicator, smith
from game import potential_game
from testergame import F_payoff


def discrete(x, n_strategy, dynamics_option):
    """離散時間でのダイナミクス

    Parameters:
    ----------
    初期状態
    x : list[float]
    戦略数
    n_strategy : int

    Returns:
    ----------
    x_data : list
    p_data : list
       ダイナミクスのシミュレーションデータ
    """
    x_data = [[] for _ in range(n_strategy)]
    p_data = [[] for _ in range(n_strategy)]

    for _ in range(count):
        p = F_payoff(x)
        if "BNN" in dynamics_option:
            rho = bnn(x, p)
        if "レプリケータ" in dynamics_option:
            rho = replicator(x, p)
        if "スミス" in dynamics_option:
            rho = smith(x, p)
        tmp_x = []

        for index in range(n_strategy):
            dx = [0 for _ in range(n_strategy)]

            for sub_index in range(n_strategy):
                dx[index] += x[sub_index] * rho[sub_index][index]
                dx[index] -= x[index] * rho[index][sub_index]

            tmp_x.append(x[index] + epsilon * dx[index])
            p_data[index].append(p[index])
            x_data[index].append(x[index])

        x = tmp_x.copy()
    return x_data, p_data


if __name__ == "__main__":
    st.title("数値シミュレーション作成")

    st.sidebar.title("変数の設定")
    dynamics_option = st.sidebar.radio(
        "ダイナミクスを選択してください:",
        (
            "レプリケータダイナミクス（他プレイヤーを模倣）",
            "BNNダイナミクス（平均より高い利得を選択）",
            "スミスダイナミクス（他戦略と現在の戦略を比較）",
        ),
    )
    x_1 = st.sidebar.slider("初期状態1：", 0.0, 1.0)
    st.sidebar.write("初期状態2:", 1 - x_1)

    count = 1000
    epsilon = st.sidebar.number_input("ステップサイズ", 0.00, 5.0, 0.01)

    count_size = st.sidebar.number_input("横軸", 10, 1000, 1000)

    x = [x_1, 1 - x_1]
    n_strategy = 2

    x_data, p_data = discrete(x, n_strategy, dynamics_option)

    t_all = np.arange(0, count)

    fig = plt.figure()
    x1 = plt.plot(t_all, x_data[0])
    x2 = plt.plot(t_all, x_data[1], linestyle="dashed")

    plt.xlabel("time k")
    plt.ylabel("state w")
    plt.xlim(0, count - 1)
    plt.legend((x1[0], x2[0]), ("w_1", "w_2"), loc=1)
    plt.xlim(0, count_size)
    plt.grid()

    st.pyplot(fig)

    fig = plt.figure()
    p1 = plt.plot(t_all, p_data[0])
    p2 = plt.plot(t_all, p_data[1], linestyle="dashed")

    plt.xlabel("time k")
    plt.ylabel("payoff f")
    plt.xlim(0, count - 1)
    plt.legend((p1[0], p2[0]), ("f_1", "f_2"), loc=1)
    plt.xlim(0, count_size)
    plt.grid()

    st.pyplot(fig)
