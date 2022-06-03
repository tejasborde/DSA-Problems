import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')

# Smallest subarray with sum greater than x
# Input:
# A[] = {1, 4, 45, 6, 0, 19}
# x  =  51
# Output: 3
# Explanation:
# Minimum length subarray is 
# {4, 45, 6}


# arr=[225]
# n=len(arr)
# X=197


#Solution 1 :  Bruteforce TC-O(n^2) and SC-O(1)

# def smallestSubArrayLengthwithSumGreaterThanX(arr,n,X):

#     minLength=999999
#     for  i in range(n):
#         s=0
#         for j in range(i,n):
#             s+=arr[j]
#             if(s>X):
#                 minLength=min(minLength,j-i+1)
#     return minLength


#===========================================================================

#Solution 2 :   TC-O(n) and CS-O(1)
#Two Pointer approach - Sliding window technique

# def smallestSubArrayLengthwithSumGreaterThanX(arr,n,x):
#     minLength=999999
#     i=0
#     j=0
#     s=0
#     while(i<=j and j<n):
#         while(s<=x and j<n):
#             s+=arr[j]
#             j+=1
#         while(s>x and i<j):
#             minLength=min(minLength,j-i)
#             s-=arr[i]
#             i+=1

#     return minLength
    

# print(smallestSubArrayLengthwithSumGreaterThanX(arr, n, X))













