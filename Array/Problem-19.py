import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# Common elements
# Input:
# n1 = 6; A = {1, 5, 10, 20, 40, 80}
# n2 = 5; B = {6, 7, 20, 80, 100}
# n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20 80
# Explanation: 20 and 80 are the only
# common elements in A, B and C.


A=[1, 5, 10, 20, 40, 80]
B=[6, 7, 20, 80, 100]
C=[3, 4, 15, 20, 30, 70, 80, 120]

n1=len(A)
n2=len(B)
n3=len(C)


def commonElements (A, B, C, n1, n2, n3):
    res = []
    i = 0
    j = 0
    k = 0
    while(i < n1 and j < n2 and k < n3):
        a = A[i]
        b = B[j]
        c = C[k]
        
        
        if(a == b == c and a not in res):
            res.append(a)
            i+=1
            j+=1
            k+=1
            
        elif(a < b):
            i += 1
            
        elif(b < c):
            j += 1
            
        else:
            k += 1
            
    return res


print(commonElements(A, B, C, n1, n2, n3))