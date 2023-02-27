import itertools

"""
Basically the question means if the number is 3 so the possible number of outcome will be 8.
BBB
BBR
BRB
BRR 
RBB
RBR
RRB
RRR 
But the number of sequeces where R is more or equal is only 4, i.e., BRR, RBR, RRB, RRR. So that is what I need as the output.
So, to get that I used itertools for storing all the outcomes in a list and then removing the ones with more number of B, after that counting the number of elements in the new list.
"""

def boolean_table(x):
    variables = ['R', 'B']
    combinations = itertools.product(variables, repeat=x)
    return list(map(''.join, combinations))

T = int(input())

for _ in range(T):
    N = int(input())
    X=[]
    L = boolean_table(N)
    countR, countB = 0, 0
    for i in L:
        for j in i:
            if j=="R":
                countR+=1
            else:
                countB+=1
        if countR>=countB:
            X.append(i)
            countR = countB = 0
        
    print(len(X))
