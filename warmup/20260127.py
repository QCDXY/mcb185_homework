def is_prob(x):
    if x <=1 and x >= 0:
        return True
    else:
        return False
    
def distance(x1, y1, x2, y2):
    return ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)) ** 0.5
