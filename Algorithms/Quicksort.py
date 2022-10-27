from random import randint
def Partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j]<=x:
            i+=1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def QuickSort(A, p, r):
    if (p<=r):
        q = Partition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)

def RandomizedPartition(A, p, r):
    i = randint(p, r)
    A[r], A[i] = A[i], A[r]
    return Partition(A, p, r)

def RandomizedQuickSort(A, p, r):
    if (p<=r):
        q = RandomizedPartition(A, p, r)
        RandomizedQuickSort(A, p, q-1)
        RandomizedQuickSort(A, q+1, r)

def TailRecursiveQuickSort(A, p, r):
    while (p<r):
        q = Partition(A, p, r)
        QuickSort(A, p, q-1)
        p = q+1

def RandomizedSelect(A,p, r, i):
    if p==r:
        return A[p]
    q = RandomizedPartition(A, p, r)
    k = q-p+1
    if i==k:
        return A[q]
    elif i<k:
        return RandomizedSelect(A, p, q-1, i)
    else:
        return RandomizedSelect(A, q+1, r, i-k)

A = list("QUICKSORT")
QuickSort(A, 0, 8)
print(A)