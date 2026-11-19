import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Your code here
    mean=np.mean(data,axis=0)
    std=np.std(data,axis=0)
    min=np.min(data,axis=0)
    max=np.max(data,axis=0)
    norm=[]
    for i in range(len(data)):
        l=[]
        for j in range(len(data[0])):
            l.append((data[i][j]-min[j])/(max[j]-min[j]))
        norm.append(l)
    
    std1=(data-mean)/std
    
    return std1,norm

    pass