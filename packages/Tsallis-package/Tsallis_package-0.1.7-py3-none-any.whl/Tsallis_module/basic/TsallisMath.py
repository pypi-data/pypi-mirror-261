import array
import numpy as np
def qexp(x=0, q=1.0, type=1):
    # x -> Value to calculate
    # q -> deformation parameter q of Tsallis statistics
    # type -> type of the distribution. There are two types of distributions, 1rst is with e_(2-q) and the other is with e_q functions
    if q == 1: return np.exp(x) 
    if type !=1 and type != 2: raise AttributeError
    if isinstance(x, float) or isinstance(x, np.float64):
        #error management
        #body
        match type:
            case 1:
                y = 1+(q-1)*x 
                if y<=0:
                    y = 0
                else:
                    y = pow(y,1.0/(q-1))
            case 2:
                y = 1+(1-q)*x 
                if y<=0:
                    y = 0
                else:
                    y = pow(y,1.0/(1-q))
            case _:
                y = 1+(q-1)*x 
                if y<=0:
                    y = 0
                else:
                    y = pow(y,1.0/(q-1))
        return y
    elif isinstance(x,list):
        y = []
        for x_element in x:
            y.append(qexp(x_element,q,type))
        return y
        
def qlog(x=1.0, q=1.0, type=1):
    # x -> Value to calculate
    # q -> deformation parameter q of Tsallis statistics
    # type -> type of the distribution. There are two types of distributions, 1rst is with e_(2-q) and the other is with e_q functions
    if q == 1: return np.log(x) 
    if type !=1 and type != 2: raise AttributeError
    if isinstance(x, float) or isinstance(x, np.float64):
        #error management
        #body
        match type:
            case 1: 
                if x>0:
                    y = (pow(x,1/(q-1))-1)/(q-1)
                else:
                    raise ValueError('Value must be possitive')
            case 2:
                if x>0:
                    y = (pow(x,1/(1-q))-1)/(1-q)
                else:
                    raise ValueError('Value must be possitive')
            case _:
                if x>0:
                    y = (pow(x,1/(q-1))-1)/(q-1)
                else:
                    raise ValueError('Value must be possitive')
        return y
    elif isinstance(x,list):
        y = []
        for x_element in x:
            y.append(qlog(x_element,q,type))
        return y
    
def qX(x=1.0, q=1.0, type=1):#type could be 1,2,3
        if q==1.0: return x
        if type !=1 and type != 2: raise AttributeError
        if isinstance(x, float):
             return 1/(q-1)*np.log(1+(q-1)*x)
        elif isinstance(x,list):
            y = []
            for x_element in x:
                y.append(qX(x_element,q,type))
            return y