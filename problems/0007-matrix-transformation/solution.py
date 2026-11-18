import numpy as np
def det(matrix:list[list[int|float]])->float:
    return np.linalg.det(matrix)
def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    if(det(T)==0 or det(S)==0):
        return -1
    x=det(T)
    T=np.linalg.inv(T)
    A=np.array(A)
    T=np.array(T)
    S=np.array(S)
    return(T@A@S)
    pass