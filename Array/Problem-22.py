#Find factorial 
# Input: N = 5
# Output: 120
# Explanation : 5! = 1*2*3*4*5 = 120

import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')

N=6


#Solution 1 : without recusion
# def factorial(N):
#     ans=1 
#     while(N!=1):
#         ans=N*ans 
#         N-=1 
#     return ans 


#Solution 2 : with recursion
def factorial(N):
    if(N==1):
        return N 
    return N*factorial(N-1) 

print(factorial(N))