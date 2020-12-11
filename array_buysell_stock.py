A = [1,2,3,4,5,7,9]

# Time Complexity : O(n^2)
# Space Complexity : O(1)
def buy_sell_stock_naive(A):
    max_profit = 0
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[j]-A[i] > max_profit:
                max_profit = A[j] - A[i]
    return max_profit

# Time Complexity : O(n)
# Space Complexity : O(1)
def buy_sell(A):
    max_profit = 0
    min_price = A[0]
    for price in A:
        min_price = min(min_price,price)
        compare_profit = price - min_price
        max_profit = max(compare_profit,max_profit)
    return max_profit

print(buy_sell_stock_naive(A))
print(buy_sell(A))
