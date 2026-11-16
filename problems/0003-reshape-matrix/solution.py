import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    m=len(a)
    n=len(a[0])
    
    x=new_shape[1]
    z=new_shape[0]
    c=0
    k=0
    y=[]
    l=[]
    for i in range(m):
        
        for j in range(n):
            l.append(a[i][j])
            c+=1
            if c==x:
                y.append(l)
                k+=1
                l=[]
                c=0
            if k>z:
                return []
    
    return y

    pass