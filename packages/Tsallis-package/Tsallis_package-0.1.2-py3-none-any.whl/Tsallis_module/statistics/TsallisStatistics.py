import numpy as np
from ..basic import qMath

def validate_prob(probability_vector, exact=False):
    if not exact:
        return sum(probability_vector) <= 1
    else:
        return sum(probability_vector) == 1

def qEntropy(q,probability,k=1.0):
    if validate_prob(probability) and q != 1:
        Sq=k*(1-sum(probability**q))/(q-1)
    elif validate_prob(probability) and q == 1:
        Sq = k*sum(np.log(probability))
    else:
        raise ValueError("Probabilties must sum up to 1")
        return probability*0
    return Sq

def Zq(q,Energy_set):
    Z = 0
    qM = qMath(q,type)
    for E in Energy_set:
        Z += qM.qexp(E)
    return Z

def qProbability(Z,Energy_value, vector = False):
    qM = qMath()
    P=[]
    if Z>0:
        if not vector:
            P.append(qM.qexp([Energy_value])/Z)
            return P
        else:
            for E in Energy_value:
                P.append(qM.qexp(E)/Z)
            return P
    else:
        raise ValueError("The partition function must be a possitive value")
        return 0
    
def qProb_and_Z( h, J, beta, qM):
    Z = 0.0
    P = []
    n = len(h)
    ns = 2**n
    Energy_set = []
    for i in np.arange(0,ns):
        sigma = 2*num2binint(i,n)-1
        E = qIsing(sigma,h,J,qM.q)
        Energy_set.append(E)
        P.append(qM.qexp(-beta * E))
        Z += P[i]

    P = np.asarray(P)
    P /= Z

    return  P, Z, Energy_set

def qIsing(sigma, h, J, q):
    import numpy as np
    H = 0
    n = len(h)
    #sigma2 = sigma_mat(sigma)
    for i in np.arange(0,n):
        H -= h[i]*(sigma[i]-np.sign((1-q)*h[i]))
        for ii in np.arange(i,n):
            if ii>i:
                H -= J[i][ii]*(sigma[i]*sigma[ii]-np.sign((1-q)*J[i][ii]))
    return H
            
def sigma_mat(sigma):
    import numpy as np
    n = len(sigma)
    sigma_mat = np.zeros((n,n))
    for i in np.arange(0,n-1):
        for ii in np.arange(i,n):
            sigma_mat[i][ii] = sigma[i]*sigma[ii]
    return sigma_mat

def sigma_mat3(sigma):
    import numpy as np
    n = len(sigma)
    sigma_mat3_ = np.zeros((n,n,n))
    for i in np.arange(0,n):
        for ii in np.arange(0,n):
            for iii in np.arange(0,n):
                if iii>ii and ii>i:
                    sigma_mat3_[i][ii][iii] = sigma[i]*sigma[ii]*sigma[iii]
    return sigma_mat3_

def num2binint(decimal,n):
    binary_vector = bin(decimal).replace("0b","").zfill(n+1)[1:n+1]
    return np.asarray([int(i) for i in binary_vector])

def generate_Jh(n, type = 'normal', mu  = 0, var = 0.25, seed = None):
    import numpy as np
    np.random.default_rng(seed=seed)
    if type == 'normal':
        h = np.random.uniform(-1,1,(n))
        J = np.random.normal(mu,var,(n,n))
    elif type == 'uniform':
        h = np.random.uniform(-1,1,(n))
        J = np.random.uniform(-1,1,(n,n))
    else:
        return
    J = np.triu(J,1)
    return [h,J]

def statistical_mean(value_set,probability_set):
    if len(value_set)!=len(probability_set):
        raise AttributeError("Size of vector must be the same")
    return sum(np.multiply(value_set,probability_set))

def sigma_mean(n,P):
    ns = 2**n
    sigma_mean = np.zeros(n)
    for i in np.arange(0,ns):
        sigma_mean += (2*num2binint(i,n)-1)*P[i]
    return sigma_mean

def RMSE(vect1, vect2,n):
    return np.sqrt(sum((vect1-vect2)**2))/n