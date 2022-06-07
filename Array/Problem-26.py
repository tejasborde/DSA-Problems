import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# Maximum profit by buying and selling a share at most twice
# Input:   price[] = {10, 22, 5, 75, 65, 80}
# Output:  87
# Trader earns 87 as sum of 12, 75 
# Buy at 10, sell at 22, 
# Buy at 5 and sell at 80
# Input:   price[] = {2, 30, 15, 10, 8, 25, 80}
# Output:  100
# Trader earns 100 as sum of 28 and 72
# Buy at price 2, sell at 30, buy at 8 and sell at 80



arr=[2, 30, 15, 10, 8, 25, 80]
n=len(arr)


#Solution 1 using find max Profit with one transaction function
# def bestTimeToSellStockOneTransaction(prices,start,end,n):
#     curPrice=999999
#     profit=0

#     for i in range(start,end+1):
#         if(prices[i]<curPrice):
#             curPrice=prices[i]
#         elif(prices[i]-curPrice>profit):
#             profit=prices[i]-curPrice
#     return profit


# def bestProfitForTwoTransactions(prices,n):
#     maxProfit=0
#     for i in range(n):
#         profitLeft=bestTimeToSellStockOneTransaction(prices, 0,i, n)
#         profitRight=bestTimeToSellStockOneTransaction(prices, i+1, n-1, n)
#         maxProfit=max(maxProfit,profitLeft+profitRight)
    
#     return maxProfit



#===========================================================================

#Solution 2 using dynamic Programming 
# def bestProfitForTwoTransactions(prices,n):

#     profit=[0]*n

#     maxPrice=prices[n-1]
#     for i in range(n-2,0,-1):
#         if(prices[i]>maxPrice):
#             maxPrice=prices[i]
#         profit[i]=max(profit[i+1],maxPrice-prices[i])

#     minPrice=prices[0]
#     for i in range(1,n):
#         if(prices[i]<minPrice):
#             minPrice=prices[i]
#         profit[i]=max(profit[i-1],profit[i]+prices[i]-minPrice)
    
#     return profit[n-1]

#==============================================================================
#Solution 3 :

def bestProfitForTwoTransactions(arr, size):
    first_buy = -sys.maxsize
    first_sell = 0
    second_buy = -sys.maxsize
    second_sell = 0
 
    for i in range(size):
 
        first_buy = max(first_buy, -arr[i])
        first_sell = max(first_sell, first_buy + arr[i])
        second_buy = max(second_buy, first_sell - arr[i])
        second_sell = max(second_sell, second_buy + arr[i])
 
    return second_sell

#==============================================================================

print(bestProfitForTwoTransactions(arr, n))