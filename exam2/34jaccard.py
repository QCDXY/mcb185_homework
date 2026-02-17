import sys

def get_names(filename):
    names = []
    with open(filename) as f:
        name = f.read()
    names = name.split('\n')
    while(True):
        try:
            names.remove('')
        except ValueError:
            break
    names = set(names)
    return names


def jaccard(X,Y):
    intersection = X & Y
    union = X | Y
    if len(union) == 0.0:
        return 0.0
    return len(intersection)/len(union)

def get_names1(filename):
    names = []
    with open(filename) as f:
        name = f.read()
    names = name.split('\n')
    while(True):
        try:
            names.remove('')
        except ValueError:
            break
    unique = []
    for each in names:
        if each not in unique:
            unique.append(each)
    return unique


def jaccard1(X,Y):
    intersection = []
    for each in X:
        if each in Y:
            intersection.append(each)
    
    union = []
    for each in X:
        if each not in union:
            union.append(each)
    for each in Y:
        if each not in union:
            union.append(each)

    if len(union) == 0.0:
        return 0.0
    return len(intersection)/len(union)

files1, files2 = sys.argv[1], sys.argv[2]

set1 = get_names(files1)
set2 = get_names(files2)

list1 = get_names1(files1)
list2 = get_names1(files2)

result = jaccard(set1,set2)
result1 = jaccard1(list1,list2)

print(f'Jaccard score of this two file is :{result}')
print(f'Jaccard score of this two file is :{result1}')