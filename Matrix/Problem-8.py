import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# Rotate a matrix by 90 degree 
# in clockwise direction without using any extra space

# Input:
# 1 2 3 
# 4 5 6
# 7 8 9  
# Output:
# 7 4 1 
# 8 5 2
# 9 6 3

mat= [[1, 2,3],
     [4,5, 6],
     [7,8,9]]

rows=len(mat)
cols=len(mat[0])



#Solution 1 : Bruteforce  - space complexity - O(n^2)
#Create new matrix of row x col
#store 0th row of first mat to nth col of second matrix
#store 1th row of first mat to (n-1)th col of second matrix
#So on...
#store last row of first mat to 0th col of second matrix


#========================================================
# Solution 2     - space complexity - O(1)
#Take transpose of matrix 
#Reverse each row
def printMatrix(mat):
    for i in range(len(mat)):
        print(mat[i])


def transposeMatrix(mat,rows,cols):
    for i in range(rows):
        for j in range(i):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]


def roateMatrixByNinetyDegreesClockwise(mat,rows,cols):
    print("Before : ")
    printMatrix(mat)
    transposeMatrix(mat, rows, cols)

    for i in range(rows):
        curRow=mat[i]
        curRow.reverse()
        mat[i]=curRow
    print("After : ")
    printMatrix(mat)



# roateMatrixByNinetyDegreesClockwise(mat, rows, cols)






#Rotate Matrix by 90 degress Anti-clockwise 

#Solution 1 : bruteforce with extra space
#Take 0th row reverse it and give it 0th col of second matrix
#Take 1th row reverse it and give it thth col of second matrix
#So on till last row


#===============================
# Solution 2     - space complexity - O(n)
#Reverse each row
#Take transpose of matrix 

def roateMatrixByNinetyDegreesAntiClockwise(mat,rows,cols):
    print("Before : ")
    printMatrix(mat)
    for i in range(rows):
        curRow=mat[i]
        curRow.reverse()
        mat[i]=curRow
    
    transposeMatrix(mat, rows, cols)

    print("After : ")
    printMatrix(mat)

roateMatrixByNinetyDegreesAntiClockwise(mat, rows, cols)