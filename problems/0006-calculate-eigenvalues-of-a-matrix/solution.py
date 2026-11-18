import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    trace=matrix[0][0]+matrix[1][1]
    det=matrix[0][0]*matrix[1][1]-matrix[1][0]*matrix[0][1]
    delta=trace**2-4*det
    l=[]
    
    l.append((trace-np.sqrt(delta))/2)
    l.append((trace+np.sqrt(delta))/2)
    
    l=sorted(l,reverse=True)
    return l


    pass