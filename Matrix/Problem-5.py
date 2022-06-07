import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# Sorted matrix
# Given an NxN matrix Mat. Sort all elements of the matrix.

# Input:
# N=4
# Mat=[[10,20,30,40],
# [15,25,35,45] 
# [27,29,37,48] 
# [32,33,39,50]]
# Output:
# 10 15 20 25 
# 27 29 30 32
# 33 35 37 39
# 40 45 48 50
# Explanation:
# Sorting the matrix gives this result.


mat=[[10,20,30,40],
[15,25,35,45] ,
[27,29,37,48] ,
[32,33,39,50]]
rows=len(mat)
cols=len(mat[0])


#Solution 1 : Bruteforce using auxilary array and sorting the array
# def sortMatrix(mat,rows,cols):
#     print("Before : ",mat)
#     arr=[]
#     for i in range(rows):
#         for j in range(cols):
#             arr.append(mat[i][j])
    
#     arr.sort()

#     for i in range(rows):
#         for j in range(cols):
#             mat[i][j]=arr[0]
#             arr.pop(0)
#     print("After : ",mat)


#Solution 2 : using minheap

import heapq

def sortMatrix(mat,rows,cols):
    # print("Before : ",mat)
    arr=[]
    for i in range(rows):
        for j in range(cols):
            arr.append(mat[i][j])
    heapq.heapify(arr)
    row=0
    col=0

    while(True and row<rows):
        if(len(list(arr))==0):
            break
        else:
            popedNumber=heapq.heappop(arr)
            if(popedNumber):          
                mat[row][col]=popedNumber
                if(col==cols-1):
                    col=0
                    row+=1
                else:
                    col+=1
    # print("After : ",mat)



sortMatrix(mat, rows, cols)






