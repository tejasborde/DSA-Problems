import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')

# Minimum swaps and K together 
# Input : 
# arr[ ] = {2, 1, 5, 6, 3} 
# K = 3
# Output : 
# 1
# Explanation:
# To bring elements 2, 1, 3 together,
# swap index 2 with 4 (0-based indexing),
# i.e. element arr[2] = 5 with arr[4] = 3
# such that final array will be- 
# arr[] = {2, 1, 3, 6, 5}



# arr=[4 ,11 ,6 ,5 ,11, 20, 19, 14, 14, 2, 9, 20, 11, 11, 15, 1 ,7 ,12 ,19, 9]
# n=len(arr)
# k=14

# arr=[20, 12, 17]
# n=len(arr)
# k=6

# arr=[8 ,13 ,7, 6,4 ,8 ,5, 15 ,11 ,13 ,18]
# n=len(arr)
# k=9


# arr = [2, 1, 5, 6, 3]
# k = 3
# n=len(arr)


#=========================================================================
#Solution 1 : Bruteforce  O(n^2)

# def minSwapsKTogether(arr,n,k):
#     requiredWindowSize=0
#     for i in range(n):
#         if(arr[i]<=k):
#             requiredWindowSize+=1
#     if(requiredWindowSize==0):
#         return 0
#     badNumbers=0
#     for i in range(requiredWindowSize):
#         if(arr[i]>k):
#             badNumbers+=1
    

#     minSwaps=badNumbers

#     for i in range(n-requiredWindowSize+1):
#         curWindow=arr[i:i+requiredWindowSize]
#         badNumbers=0
#         for x in curWindow:
#             if(x>k):
#                 badNumbers+=1
#         minSwaps=min(minSwaps,badNumbers)
#     return minSwaps

#=========================================================================

#Solution 2 : O(n)
#Using Sliding Window method

# def minSwapsKTogether(arr,n,k):
#     requiredWindowSize=0

#     for i in range(n):
#         if(arr[i]<=k):
#             requiredWindowSize+=1
#     if(requiredWindowSize==0):
#         return 0
#     badNumbers=0
#     for i in range(requiredWindowSize):
#         if(arr[i]>k):
#             badNumbers+=1
    

#     start=0
#     end=requiredWindowSize
    
#     minSwaps=badNumbers
    
#     while(end<n):
#         if(arr[start]>k):
#             badNumbers-=1
#         if(arr[end]>k):
#             badNumbers+=1
#         minSwaps=min(minSwaps,badNumbers)
#         start+=1
#         end+=1
    
#     return minSwaps
    
#=========================================================================

# print(minSwapsKTogether(arr, n, k))
    














