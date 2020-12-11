
# Time Complexity = O(n^2)
# Space Complexity = 0(1)
def two_sum_naive(A,target):    
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i]+A[j]==target:
                print(f"{A[i]},{A[j]}")
                return True
    return False

# Time Complexity = O(n)
# Space Complexity = 0(n)
def two_sum_hs(A,target):
    ht = {}
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]],A[i])
            return True
        else:
            ht[target-A[i]] = A[i]  
    return False

# for sorted array
def two_sum_sorted(A, target):
    i = 0 
    j = len(A)-1
    while i<=j:
        if A[i]+A[j]==target:
            print(A[i],A[j])
            return True
        elif A[i]+A[j]< target:
            i += 1
        else:#A[i] +A[j] > target
            j -= 1
    return False

A = [1,2,3,5,4]
target = 9
# print(two_sum_naive(A,target))
# print(two_sum_hs(A,target))
print(two_sum_sorted(A,target))