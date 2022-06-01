#Find the repeated number 
# Input: nums = [1,3,4,2,2]
# Output: 2

import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')

arr=[1, 6, 3, 1, 3, 6, 6]
n=len(arr)


#Solution 1 with O(n) and extra space and modifying the original array
# def findDuplicate(arr,n):
#     for i in range(n):
#         index=arr[i]%n
#         arr[index]+=n 
    
#     for i in range(n):
#         if(arr[i]/n>=2):
#             print(i,end=" ")




#Solution 2 with O(n) and O(1) extra space

# def findDuplicate(arr,n):
#     slow=arr[0]
#     fast=arr[0]
#     while(True):
#         slow=arr[slow]
#         fast=arr[arr[fast]]
#         if(slow==fast):
#             break
#     fast=arr[0]

#     while(slow!=fast):
#         slow=arr[slow]
#         fast=arr[fast]
#     print(slow)


# findDuplicate(arr, n)