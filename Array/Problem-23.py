# Maximum Product Subarray
# Input:
# N = 5
# Arr[] = {6, -3, -10, 0, 2}
# Output: 180
# Explanation: Subarray with maximum product
# is [6, -3, -10] which gives product as 180.

import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')

arr=[ 6, -3, -10, 0, 2]
n=len(arr)


# Solution 1: Bruteforce O(n^3)
# def maxSubArrayProdcut(arr,n):
#     maxProduct=1
#     for i in range(n):
#         for j in range(i,n):
#             product=1
#             for x in arr[i:j]:
#                 product*=x 
#             maxProduct=max(maxProduct,product)

#     return maxProduct

def maxSubArrayProdcut(arr,n):
    ma=arr[0]
    mi=arr[0]
    ans=arr[0]

    for i in range(1,n):
        if(arr[i]<0):
            ma,mi=mi,ma 
        ma=max(ma*arr[i],arr[i])
        mi=min(mi*arr[i],arr[i])
        ans=max(ans,ma)
    return ans 

print(maxSubArrayProdcut(arr, n))