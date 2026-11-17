import numpy as np
def det3x3(matrix: list[list[int|float]]) -> float:
    return round(np.linalg.det(matrix),10)

def determinant_4x4(matrix: list[list[int|float]]) -> float:
    # Your recursive implementation here
    det=0
    for k in range(4):
        x=[]
        for i in range(1,4):
            l=[]
            for j in range(4):
                if k!=j:
                    l.append(matrix[i][j])
            x.append(l)
        if k%2==0:
            det+=det3x3(x)*matrix[0][k]
        else:det-=det3x3(x)*matrix[0][k]
    return det
        


    pass