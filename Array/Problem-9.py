# Minimise the maximum difference between heights [V.IMP]
# https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1

# Input:
# K = 2, N = 4
# Arr[] = {1, 5, 8, 10}
# Output:
# 5
# Explanation:
# The array can be modified as 
# {3, 3, 6, 8}. The difference between 
# the largest and the smallest is 8-3 = 5.

import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


arr=[1, 5, 8, 10]
n=len(arr)
k=2

def minThemaxDiffBetwheight(arr,n,k):
    arr.sort()
    minimum=arr[0]
    maximum=arr[n-1]

    res=maximum-minimum

    for i in range(1,n):
        minimum=min(arr[i]-k,arr[0]+k)
        maximum=max(arr[i-1]+k,arr[n-1]-k)
        
        res=min(res,maximum-minimum)
    return res 
print(minThemaxDiffBetwheight(arr, n, k))