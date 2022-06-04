import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')


# Zigzag (or diagonal) traversal of Matrix


# Input
# 1     2     3     4
# 5     6     7     8
# 9    10    11    12
# 13    14    15    16
# 17    18    19    20

# Output
# 1
# 5 2
# 9 6 3
# 13 10 7 4
# 17 14 11 8
# 18 15 12
# 19 16
# 20


# matrix=[[1,2,3,4],
#        [5,6,7,8],
#        [9,10,11,12],
#        [13,14,15,16],
#        [17,18,19,20]]

# matrix = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]


matrix =[[1, 2],
     [3, 4]]

rows=len(matrix)
cols=len(matrix[0])




#Solution 1 
# def traverseMatrixDiagonally(matrix,rows,cols):
#     ans=[]
#     rows1=rows
#     if(rows!=cols):
#         rows1-=1
#     rowCounter=0
#     while(rowCounter<rows1):
#         row=0
#         col=rowCounter
#         while(row<=rowCounter and col>=0):
#             print(matrix[row][col],end=" ")
#             ans.append(matrix[row][col])
#             row+=1
#             col-=1
#         print()
#         rowCounter+=1
    
#     rowCounter=1
#     while(rowCounter<rows):
#         col=cols-1
#         row=rowCounter
#         while(row<rows and col>=0):
#             print(matrix[row][col],end=" ")
#             ans.append(matrix[row][col])
#             row+=1
#             col-=1
#         print()
#         rowCounter+=1
#     return ans

#=================================================================

# Solution 2
def traverseMatrixDiagonally(arr, rows, cols):
    ans = [[] for i in range(rows + cols - 1)]
     
    for i in range(cols):
        for j in range(rows):
            ans[i + j].append(arr[j][i])
     
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end = " ")
        print()
    return ans


#===================================================================
print(traverseMatrixDiagonally(matrix, rows, cols))



