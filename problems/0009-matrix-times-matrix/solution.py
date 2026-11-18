import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    a=np.matrix(a)
    b=np.matrix(b)
    n=np.shape(a)
    
    m=np.shape(b)
    if n[1]!=m[0]:
        return -1
    
    c=a@b
    return c