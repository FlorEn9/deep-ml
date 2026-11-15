def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    x=[]
    v=len(a)
    w=len(a[0])
    for i in range(w):
        p=[]
        for j in range(v):
            p.append(a[j][i])
        x.append(p)

    
    
    return x
    pass