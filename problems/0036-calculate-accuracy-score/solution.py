import numpy as np

def accuracy_score(y_true, y_pred):
    # Your code here
    x=y_pred==y_true
    return (np.sum(x)/len(y_pred))
    pass