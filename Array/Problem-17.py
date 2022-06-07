import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')



# Best Time to Buy and Sell Stock
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

prices = [3,7,1,5,3,6,4]
n=len(prices)


#Solution 1 : O(n^2)
# def bestTimeToSellStock(prices,n):
#     profit=0

#     for i in range(n):
#         for j in range(i+1,n):
#             if(prices[j]-prices[i]>profit):
#                 profit=prices[j]-prices[i]
#     return profit

#Solution 2 :

# def bestTimeToSellStock(prices,n):
#     cur=0
#     next=1
#     profit=0

#     while(next<n):
#         if(prices[cur]<prices[next]):
#             curProfit=prices[next]-prices[cur]
#             profit=max(profit,curProfit)
#         else:
#             cur=next 
#         next+=1
#     return profit 



#Solution 3 :

def bestTimeToSellStock(prices,n):
    curPrice=999999
    profit=0

    for i in range(n):
        if(prices[i]<curPrice):
            curPrice=prices[i]
        elif(prices[i]-curPrice>profit):
            profit=prices[i]-curPrice
    return profit 

print(bestTimeToSellStock(prices, n))













