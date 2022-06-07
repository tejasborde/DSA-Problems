import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')

#Mereg Two Sorted arrays
# Input:
# N = 4, M = 5
# arr1[] = {1, 3, 5, 7}
# arr2[] = {0, 2, 6, 8, 9}
# Output: 0 1 2 3 5 6 7 8 9
# Explanation: Since you can't use any 
# extra space, modify the given arrays
# to form 
# arr1[] = {0, 1, 2, 3}
# arr2[] = {5, 6, 7, 8, 9}

a1=[1, 3, 5, 7]
a2=[0, 2, 6, 8, 9]
m=len(a1)
n=len(a2)


#Solution 1 Using Extra Space
# def mergeTwoSortedArrays(a1,m,a2,n):
#     print("Before : ")
#     print(*a1)
#     print(*a2)
#     arr=[]
#     for num in a1:
#         arr.append(num)
#     for num in a2:
#         arr.append(num)
    
#     arr.sort()
#     cur=0
#     for i in range(m):
#         a1[i]=arr[cur]
#         cur+=1
#     for i in range(m):
#         a2[i]=arr[cur]
#         cur+=1
    
#     print("After : ")
#     print(*a1)
#     print(*a2)

#Solution 2 Using Comparison
# def mergeTwoSortedArrays(a1, m, a2, n):
#     i=0
#     j=0
#     print("Before : ")
#     print(*a1)
#     print(*a2)
#     while(i<m and j<n):
#         if(a1[i]>a2[j]):
#             a1[i],a2[j]=a2[j],a1[i]
#             i+=1
#             a2.sort()
    
#     print("After : ")
#     print(*a1)
#     print(*a2)



#Solution 3 Using Gap method
import math
def mergeTwoSortedArrays(a1,m,a2,n):
    gap=math.floor((m+n)/2.0)
    arr=[]
    for i in a1:
        arr.append(i)
    for i in a2:
        arr.append(i)
    
    while(gap>0):
        cur=0
        next=cur+gap
        while(next<(m+n)):
            if(arr[cur]>arr[next]):
                arr[cur],arr[next]=arr[next],arr[cur]
            cur+=1
            next=cur+gap
        gap=math.floor((gap)/2.0)

    cur=0
    for i in range(m):
        a1[i]=arr[cur]
        cur+=1
    for i in range(m):
        a2[i]=arr[cur]
        cur+=1

    print("After : ")
    print(*a1)
    print(*a2)
mergeTwoSortedArrays(a1, m, a2, n)