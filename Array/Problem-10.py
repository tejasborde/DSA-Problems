#Minimum number of jumps 
# Input:
# N = 11 
# arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} 
# Output: 3 
# Explanation: 
# First jump from 1st element to 2nd 
# element with value 3. Now, from here 
# we jump to 5th element with value 9, 
# and from here we will jump to last. 

import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')

arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n=len(arr)


#Solution 1 : O(n^2) and o(n) extra space

# import sys

# def minjumpsToreachendofArr(arr,n):
#     dp=[sys.maxsize for i in range(n)]
#     dp[0]=0

#     for i in range(n):
#         for j in range(0,i):
#             if(dp[j]!=sys.maxsize and arr[j]+j>=i):
#                 if(dp[j]+1<dp[i]):
#                     dp[i]=dp[j]+1
#     return dp[n-1]



#Solution 2 : O(n)
def minjumpsToreachendofArr(arr,n):
    maxReachable=arr[0]
    step=arr[0]
    jump=1

    if(n==1):
        return 0
    elif(arr[0]==0):
        return -1
    else:
        for i in range(1,n):
            if(i==n-1):
                return jump
            maxReachable=max(maxReachable,i+arr[i])
            step-=1

            if(step==0):
                jump+=1
                if(i>=maxReachable):
                    return -1
                step=maxReachable-i 


print(minjumpsToreachendofArr(arr, n))
            