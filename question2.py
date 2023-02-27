import itertools

def boolean_table(x):
    elements = ['R', 'B']
    combinations = itertools.product(elements, repeat=x)
    return list(map(''.join, combinations))

T = int(input())

for _ in range(T):
    N = int(input())
    X=[]
    L = boolean_table(N)
    print(L)
    countR, countB = 0, 0
    for i in L:
        for j in i:
            if j=="R":
                countR+=1
            elif j=="B":
                countB+=1
        if countR>=countB:
            X.append(i)
            countR, countB = 0, 0
    print(len(X))
