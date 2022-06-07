import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')

# Chocolate Distribution Problem 
# Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are M students, the task is to distribute chocolate packets among M students such that :
# 1. Each student gets exactly one packet.
# 2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.

# Input:
# N = 8, M = 5
# A = {3, 4, 1, 9, 56, 7, 9, 12}
# Output: 6
# Explanation: The minimum difference between 
# maximum chocolates and minimum chocolates 
# is 9 - 3 = 6 by choosing following M packets :
# {3, 4, 9, 7, 9}.


arr=[7, 3, 2, 4, 9, 12, 56]
n=len(arr)
m=3


def chocolateDistribution(arr,n,m):
    arr.sort()

    minDifference=9999999

    i=0
    while(i+m-1<n):
        dif=arr[i+m-1]-arr[i]
        minDifference=min(minDifference,dif)
        i+=1
    
    return minDifference


print(chocolateDistribution(arr, n, m))












