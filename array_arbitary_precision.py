# # one liner for adding one at the end:
# A = [9,9,9]
# num_st = "".join(map(str,A))
# ans = int(num_st)+1
# print(ans)

def plus_one(A):
    A[-1] +=1 
    for i in reversed(range(1,len(A))):
        if A[i] != 10:
            break
        A[i]=0
        A[i-1] +=1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

A1 = [1,2,5]
A2 = [9,9,9]
print(plus_one(A1))
print(plus_one(A2))
