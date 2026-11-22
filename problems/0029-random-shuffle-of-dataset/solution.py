import numpy as np

def shuffle_data(X, y, seed=None):
    # Your code here
    np.random.seed(seed)
    n=X.shape[0]
    idx=np.random.permutation(n)
    return(X[idx],y[idx])
    pass