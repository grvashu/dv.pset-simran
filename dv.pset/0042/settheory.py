#P=[4,2,3,1,6,9]
#Q=[8,1,0,3,4,2]
A=[1,2,3,4,5,6,7]
B=[3,4,5,6,9]
def union(P,Q):
    '''
    Returns a set R (Python list) which is P UNION Q
    '''
    R=[]
    for i in range (len(P)):
        R.append(P[i])
    for j in range (len(Q)):
        R.append(Q[j])
    return R
print ('union:',union(A,B))

'''
def union(P,Q):
'''
#Returns a set R (Python list) which is P UNION Q
'''
    R=[]
    for i in range (len(P)):
        R.append(P[i])
    for j in range (len(Q)):
        for k in range(len(R)):
            if Q[j]==R[k]:
                break
            else:
                R.append(Q[j])
    return R
print ('union:',union(A,B))
'''

def difference(P,Q):
    '''
    Returns a set R (Python list) which is P DIFFERENCE Q
    '''
    R=[]
    for i in range (len(P)):
        flag=0
        for j in range (len(Q)):
            if P[i]==Q[j]:
                flag=1
                break
        if flag==0:
            R.append(P[i])
    return R
print ('difference:',difference(A,B))


def is_subset(P,Q):
    '''
    Returns true if P is subset of Q
    '''
    flag=1
    i=0
    while(flag==1 and i<len(Q)):
        for j in range(len(P)):
            if P[j]==Q[i]:
                flag=1
                break
            else:
                flag=0
        i=i+1
    if flag==1:
        print("it is a subset")
    else:
        print("it is not a subset")
is_subset(A,B)


def powerset(P):
    R=[]
    R.append([P[0]])

    for i in range(1,len(P),1):
        T=[]
        for r in R:
            T.append(r[:])
        T.append([])

        for x in T:
            x.append(P[i])

        for l in T:
            R.append(l)
    return R

    '''
    Returns a set R (Python list) which is powerset of P
    '''
    '''R=[]
    for every item in P:
        T=R
        add an item of P to every item of T and add to the list R '''
print("Powerset: ",powerset(A))



def symmetric_difference(P,Q):
    '''
    union of two sets minus their intersection
    Returns a set P (Python list) which is P SYM_DIFF Q
    '''
    U=[]
    D=[]
    U.append(union(P,Q))
    D.append(difference(P,Q))
    '''for i in range (len(U)):
        for j in range (len(D)):
            if U[i]==D[j]:
                U.pop(U[i])
    '''
    R=[]
    for i in range (len(U)):
        flag=0
        for j in range (len(D)):
            if U[i]==D[j]:
                flag=1
                break
        if flag==0:
            R.append(U[i])
        return R
#    return (U)
print("symmetric difference: ",symmetric_difference(A,B))
