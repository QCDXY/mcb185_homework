import math

def is_histogram(H):
    vals = []
    total = 0
    for each in H:
        try:
            x = float(each)
        except (TypeError,ValueError):
            return False,'input include non-float value.'
        vals.append(x)
        if x < 0:
            return False,'input include negative value.'
        total += x
        
    if not math.isclose(total,1.0):
        return False,'histogram is not sum to 1.'
    return True,''
    

def dkl(P,Q):
    bool_val, msg = is_histogram(P)
    if bool_val == False: return f'It is not a valid histogram, since {msg}'
    bool_val, msg = is_histogram(Q)
    if bool_val == False: return f'It is not a valid histogram, since {msg}'
    P1 = []
    Q1 = []
    for value in P:
        P1.append(float(value))
    for value in Q:
        Q1.append(float(value))


    kl = 0.0
    for p, q in zip(P1,Q1):
        if math.isclose(p,0.0):
            continue
        if math.isclose(q,0.0):
            print('Invalid zero')
        kl += p * math.log(p/q)
    return kl

print(dkl([0.1,0.5,0.4],[0.6,0.2,0.2]))
print(dkl([0.1,0.5,0.4],[0.6,0.2,'x']))
print(dkl([0.1,0.5,0.4],[0.6,0.2,-0.2]))
print(dkl([0.1,0.5,0.4],[0.6,0.2,0.1]))