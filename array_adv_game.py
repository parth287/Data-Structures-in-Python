def array_advance_game(A):
    furthest_reach = 0
    i = 0 
    last = len(A)-1
    while i <= furthest_reach and i< last:
        furthest_reach = max(furthest_reach, A[i] + i)
        i +=1
    return furthest_reach >= last

A1 =[2,4,5,6,7]
A2 =[12,14,115,16,17]
print(array_advance_game(A1))
print(array_advance_game(A2))
