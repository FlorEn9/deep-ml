import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    s=0
    m=max(scores)
    for i in range(len(scores)):
        s+=math.exp(scores[i]-m)
    for i in range(len(scores)):
        scores[i]=math.exp(scores[i]-m)/s
    return scores
    pass