import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')


# Search in a matrix 
# Input:
# N = 3, M = 3
# mat[][] = 3 30 38 
#          44 52 54 
#          57 60 69
# X = 62
# Output:
# 0
# Explanation:
# 62 is not present in the
# matrix, so output is 0



mat=[[3 ,30 ,38 ],[44 ,52 ,54 ],[ 57 ,60 ,69]]
r=len(mat)
c=len(mat[0])
x=3



#Solution 1 : O(n^2) -TC
# def searchInmatrix(mat,r,c,x):
#     for i in range(r):
#         for j in range(c):
#             if(mat[i][j]==x):
#                 return 1
#     return 0

#==========================================================

#Solution 2

#Start from TopRight Corner
#if element < target => eliminate row
#if element > target => eliminate col
#ans
# O(m+n)-TC

# def searchInmatrix(mat,r,c,x):
#     i=0
#     j=c-1

#     while(i<r and j>=0):
#         if(mat[i][j]==x):
#             return 1
#         elif(mat[i][j]<x):
#             i+=1
#         elif(mat[i][j]>x):
#             j-=1
#     return 0


# print(searchInmatrix(mat, r, c, x))



s="I AM AWESOME"

def reverseString(s):
    # arr=[]
    # s=s[::-1]
    # for i in s:
    #     if(i!=" " and i not in arr):
    #         arr.append(i)
    # arr="".join(arr)
    # return arr
    ans=""
    s=s[::-1]
    for i in s:
        if(i!=" " and ans.count(i)==0):
            ans+=i
    return ans

print(reverseString(s))


