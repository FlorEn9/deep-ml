import numpy as np

def to_categorical(x, n_col=None):
    # Your code here
    z=max(x)+1
    if n_col!=None:
        z=n_col
    l=[]
    for i in range(len(x)):
        sublist=[]
        for j in range(z):
            if j==x[i]:
                sublist.append(1)
            else:sublist.append(0)
        l.append(sublist)
    return np.array(l)

    pass