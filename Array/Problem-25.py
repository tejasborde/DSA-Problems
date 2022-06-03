import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')

# Given an array of size n and a number k, find all elements that appear more than n/k times


arr = [ 3, 1, 2, 2, 1, 2, 3, 3 ]
n = len(arr)
k = 4


#Solution 1 using User Defined Dictionary
# def findElements(arr,n,k):
#     dic={}
#     for i in arr:
#         try:
#             dic[i]+=1 
#         except KeyError:
#             dic[i]=1
    
#     ans=[]
#     for i in arr:
#         if(dic[i]>(n//k) and (i not in ans)):
#             ans.append(i)
#     ans.sort()
#     return ans 


#Solution 2 using in built Counter Function
from collections import Counter 

def findElements(arr,n,k):
    count=Counter(arr)
    ans=[]
    for i in count:
        if(count[i]>(n//k) and (i not in ans)):
            ans.append(i)
    ans.sort()
    return ans

print(findElements(arr, n, k))


