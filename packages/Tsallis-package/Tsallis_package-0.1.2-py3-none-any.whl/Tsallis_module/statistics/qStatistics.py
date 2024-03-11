class qStatistics:
    import numpy as np
    from ..basic import qMath
    from ..statistics import TsallisStatistics as Ts
    Z = 0
    P = []

    def __init__(self) -> None:
        pass

    def __str__(self):
        return f'Z = {self.Z}, index of P = {self.P.index}'
    
    def __repr__(self):
        return f'qStatistics()'
    
    def validate_prob(self,probability_vector, exact=False):
        return self.Ts.validate_prob(probability_vector,exact)
    
    def qEntropy(self,probability,k=1.0):
        return self.qEntropy(probability,k)
    
    def Zq(self,Energy_set):
        return self.Zq(Energy_set)
    
    def qProbability(self,Energy_value, vector = False):
        return self.Ts.qProbability(self.Z,Energy_value,vector)
        
    def qProb_and_Z(self, h, J, beta, qM):    
        return  self.Ts.qProb_and_Z(h,J,beta,qM)

    def qIsing(self,sigma, h, J, q):
        H = 0
        n = len(h)
        #sigma2 = sigma_mat(sigma)
        for i in self.np.arange(0,n):
            H -= h[i]*(sigma[i]-self.np.sign((1-q)*h[i]))
            for ii in self.np.arange(i,n):
                if ii>i:
                    H -= J[i][ii]*(sigma[i]*sigma[ii]-self.np.sign((1-q)*J[i][ii]))
        return H
                
    def sigma_mat(self,sigma):
        n = len(sigma)
        sigma_mat = self.np.zeros((n,n))
        for i in self.np.arange(0,n-1):
            for ii in self.np.arange(i,n):
                sigma_mat[i][ii] = sigma[i]*sigma[ii]
        return sigma_mat

    def sigma_mat3(self,sigma):
        n = len(sigma)
        sigma_mat3_ = self.np.zeros((n,n,n))
        for i in self.np.arange(0,n):
            for ii in self.np.arange(0,n):
                for iii in self.np.arange(0,n):
                    if iii>ii and ii>i:
                        sigma_mat3_[i][ii][iii] = sigma[i]*sigma[ii]*sigma[iii]
        return sigma_mat3_

    def num2binint(self,decimal,n):
        binary_vector = bin(decimal).replace("0b","").zfill(n+1)[1:n+1]
        return self.np.asarray([int(i) for i in binary_vector])

    def generate_Jh(self,n, type = 'normal', mu  = 0, var = 0.25, seed = None):
        self.np.random.seed(seed=seed)
        if type == 'normal':
            h = self.np.random.uniform(-1,1,(n))
            J = self.np.random.normal(mu,var,(n,n))
        elif type == 'uniform':
            h = self.np.random.uniform(-1,1,(n))
            J = self.np.random.uniform(-1,1,(n,n))
        else:
            return
        J = self.np.triu(J,1)
        return [h,J]

    def statistical_mean(self,value_set,probability_set):
        return self.Ts.statistical_mean(value_set,probability_set)