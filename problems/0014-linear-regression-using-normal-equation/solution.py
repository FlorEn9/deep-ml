import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    X=np.array(X)
    T=X.T
    S=np.linalg.inv(T@X)
    theta=S@T@y
    return theta