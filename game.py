
def potential_game(x):
    '''ポテンシャルゲーム（渋滞ゲーム）
    
    Parameters:
    ----------
    x : list[float]

    Returns:
    ----------
    p : list[float]
        集団状態がxのときの利得
    '''
    
    x_1,x_2,x_3 = map(float,x)
    p = [
        -(6+4*x_1+6*(x_1+x_3)**2),
        -(6+4*x_2+6*(x_2+x_3)**2),
        -(5+4*x_3+6*(x_1+x_3)**2+6*(x_2+x_3)**2)
    ]
    return p
    
if __name__ == '__main__':
    x = [0.1,0.5,0.4]
    print(potential_game(x))