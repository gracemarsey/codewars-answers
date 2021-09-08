def invert(lst):
    inverse=[]   
    for x in lst:
        if x < 0:
            inverse.append(abs(x))
        elif x > 0:
            inverse.append(-abs(x))
        elif x == 0:
            inverse.append(0)
    return inverse