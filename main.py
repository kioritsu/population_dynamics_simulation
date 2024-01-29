import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from game import potential_game
from dynamics import bnn

def discrete(x, n_strategy):
    '''離散時間でのダイナミクス
    
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
    '''
    x_data = [[] for _ in range(n_strategy)]
    p_data = [[] for _ in range(n_strategy)]
    
    for _ in range(count):
        p = potential_game(x)
        rho = bnn(x,p)
        tmp_x = []
        
        for index in range(n_strategy):
            dx = [0 for _ in range(n_strategy)]
            
            for sub_index in range(n_strategy):
                dx[index] += x[sub_index]*rho[sub_index][index]
                dx[index] -= x[index]*rho[index][sub_index]
            
            tmp_x.append(x[index]+epsilon*dx[index])
            p_data[index].append(p[index])
            x_data[index].append(x[index])
            
        x = tmp_x.copy()
    return x_data, p_data

if __name__ == '__main__':
    st.title('ポピュレーションダイナミクス数値例作成')
    
    st.sidebar.title('変数の設定')
    
    x_1 = st.sidebar.slider('初期状態1：',0.0,1.0)
    x_2 = st.sidebar.slider('初期状態2：',0.0,1.0)
    if x_1+x_2 > 1:
        st.sidebar.write('初期状態3:×')
        st.sidebar.warning('注意: 3変数の総和が1になるように調整してください。')
    else:
        st.sidebar.write('初期状態3:',1-x_1-x_2)
    
    
    count = 1000
    epsilon = st.sidebar.number_input('ステップサイズ',0.00,5.0,0.01)
    
    x = [x_1,x_2,1-x_1-x_2]
    n_strategy = 3
    
    x_data, p_data = discrete(x, n_strategy)
    
    t_all = np.arange(0,count)

    fig = plt.figure()
    x1 = plt.plot(t_all,x_data[0])
    x2 = plt.plot(t_all,x_data[1],linestyle="dashed")
    x3 = plt.plot(t_all,x_data[2],linestyle="dashdot")
    
    plt.xlabel('time k')
    plt.ylabel('state x')
    plt.xlim(0, count-1)
    plt.legend((x1[0], x2[0],x3[0]), ("Path 1", "Path 2","Path 3"), loc=1)
    plt.grid()
    
    st.pyplot(fig)
    
        
    fig = plt.figure()
    p1 = plt.plot(t_all,p_data[0])
    p2 = plt.plot(t_all,p_data[1],linestyle="dashed")
    p3 = plt.plot(t_all,p_data[2],linestyle="dashdot")
    
    plt.xlabel('time k')
    plt.ylabel('payoff p')
    plt.xlim(0, count-1)
    plt.legend((p1[0], p2[0],p3[0]), ("Path 1", "Path 2","Path 3"), loc=1)
    plt.grid()
    
    st.pyplot(fig)
