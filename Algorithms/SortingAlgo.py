def Insertion_Sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i-=1
        A[i+1]=key
    return A

def Merge(A, p, q, r):
    L = A[p : q+1]
    R = A[q+1 : r+1]
    L.append(float("inf"))
    R.append(float("inf"))
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i]<=R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
    return A


def Merge_Sort(A, p, r):
    if p<r:
        q = (p+r)//2
        Merge_Sort(A, p, q)
        Merge_Sort(A, q+1, r)
        Merge(A, p, q, r)
    return A

def CountingSort(A, B, k):
    C = [0]*k
    for i in range(len(A)):
        C[A[i]]+=1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1):
        B[C[A[i]]] = A[i]
        C[i]-=1

def Find_Max_Crossing_Subarray(A, low, mid, high):
    left_sum = -1*float("inf")
    sum1 = 0
    max_left = mid
    for i in range(mid, low-1, -1):
        sum1 += A[i]
        if sum1>left_sum:
            left_sum = sum1
            max_left = i
    right_sum = -1*float("inf")
    sum1 = 0
    max_right = mid+1
    for j in range(mid+1, high+1):
        sum1 += A[j]
        if sum1>right_sum:
            right_sum = sum1
            max_right = j
    return (max_left, max_right, left_sum+right_sum)


def Find_Maximum_Subarray(A, low, high):
    if high==low:
        return (low, high, A[low])
    else:
        mid = (high+low)//2
        (left_low, left_high, left_sum) = Find_Maximum_Subarray(A, low, mid)
        (right_low, right_high, right_sum) = Find_Maximum_Subarray(A, mid+1, high)
        (crossing_low, crossing_high, crossing_sum) = Find_Max_Crossing_Subarray(A, low, mid, high)
        if left_sum>=right_sum and left_sum>=crossing_sum:
            return (left_low, left_high, left_sum)
        elif left_sum<=right_sum and right_sum>=crossing_sum:
            return (right_low, right_high, right_sum)
        else:
            return (crossing_low, crossing_high, crossing_sum)


print(Insertion_Sort([5, 2, 4, 6, 1, 3]))