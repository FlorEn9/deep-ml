import numpy as np
def medie(vectors: list[list[float]]) -> float:
    return np.mean(vectors)
def compute(a: list[float],b: list[float]) -> float:
    x=0
    for i in range(len(a)):
        x+=a[i]*b[i]
    x=x/(len(a)-1)

    
    
    return x
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    # Your code here
    n=np.shape(vectors)
    
    for i in range(n[0]):
        mean=medie(vectors[i])
        for j in range(n[1]):
            vectors[i][j]-=mean
    cov=[]
    for i in range(n[0]):
        l=[]
        for j in range(n[0]):
            l.append(compute(vectors[i],vectors[j]))
        cov.append(l)
    

    



        

    return cov