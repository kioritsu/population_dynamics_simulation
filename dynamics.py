def cal_mean_p(x,p):
    '''利得の平均を導出
    
    Parameters:
    ----------
    x : list[float]
    p : list[float]

    Returns:
    ----------
    rho : float
       利得の平均
    '''
    mean_p = 0
    for x_i, p_i in zip(x,p):
        mean_p += x_i*p_i
        
    return mean_p

def bnn(x,p):
    '''BNNダイナミクス
    
    Parameters:
    ----------
    x : list[float]
    p : list[float]

    Returns:
    ----------
    rho : list[float]
       利得がpのときの改訂プロトコル
    '''
    rho = []
    mean_p = cal_mean_p(x,p)
    n_strategy = len(x)
    for bfo_index in range(n_strategy):
        rho_i = []
        for aft_index in range(n_strategy):
            rho_ij = max(0, p[aft_index]-mean_p)
            rho_i.append(rho_ij)
        rho.append(rho_i)

    return rho

if __name__ == '__main__':
    x = [0.1,0.5,0.4]
    p = [-7.9, -12.86, -12.96]
    print(bnn(x,p))