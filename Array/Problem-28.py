import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# Triplet Sum in Array
# Input:
# n = 6, X = 13
# arr[] = [1 4 45 6 10 8]
# Output:
# 1
# Explanation:
# The triplet {1, 4, 8} in 
# the array sums up to 13.


arr=[1 ,4 ,45, 6, 10, 8]
n=len(arr)
x=13


#Solution 1 : Bruteforce O(n^3)

# def findTripletWithSumK(arr,n,x):
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if(arr[i]+arr[j]+arr[k]==x):
#                     return [arr[i],arr[j],arr[k]]
#     return -1 

#============================================================================

#Solution 2 using Set O(n^2) and Space complexity O(n)

# def findTripletWithSumK(arr,n,x):
#     ans=0
    
#     for i in range(n-2):
#         s=set()

#         cur=x-arr[i]

#         for j in range(i+1,n):
#             if((cur-arr[j]) in s):
#                 ans=1
#                 break
#             s.add(arr[j])
#     return ans


#===============================================================================

#Solution 3 by Sorting the array

# def findTripletWithSumK(arr,n,x):
#     ans=0

#     arr.sort()
#     for i in range(n-2):
#         left=i+1
#         right=n-1
#         while(left<right):
#             s=arr[i]+arr[left]+arr[right]
#             if(arr[i]+arr[left]+arr[right]==x):
#                 ans=1
#                 break
#             elif(arr[i]+arr[left]+arr[right]<x):
#                 left+=1
#             else:
#                 right-=1
#     return ans


#print(findTripletWithSumK(arr, n, x))












