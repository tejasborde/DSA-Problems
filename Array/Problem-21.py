# Subarray with 0 sum 
# Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

# Input:
# 5
# 4 2 -3 1 6

# Output: 
# Yes

import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')

arr=[4 ,2 , 1, 6]
n=len(arr)


# Solution 1 : Bruteforce O(n^2) Check All SubArray 

# def checkSubArrayWithSumZero(arr,n):
#     for i in range(n):
#         for j in range(i,n):
#             s=sum(arr[i:j])
#             if(s==0):
#                 return True

#     return False 


#Solution 2 : O(n)  and O(n) extra space using Set
# def checkSubArrayWithSumZero(arr,n):
#         cons_sums = set()
#         sums = 0
#         for i in arr:
#             sums += i
#             if(sums in cons_sums or sums == 0):
#                 return True
#             cons_sums.add(sums)
            
#         return False

# print(checkSubArrayWithSumZero(arr, n))






