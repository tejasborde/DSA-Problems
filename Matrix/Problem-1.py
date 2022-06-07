import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')

# Spirally traversing a matrix 
# Input:
# r = 4, c = 4
# matrix[][] = {{1, 2, 3, 4},
#            {5, 6, 7, 8},
#            {9, 10, 11, 12},
#            {13, 14, 15,16}}
# Output: 
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10



matrix = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15,16]]

rows=len(matrix)
cols=len(matrix[0])

def travereseSpirally(matrix,rows,cols):
    top=0
    down=rows-1
    left=0
    right=cols-1

    direction=0

    ans=[]

    while(top<=down and left<=right):
        if(direction==0):
            for i in range(left,right+1):
                # print(matrix[top][i],end=" ")
                ans.append(matrix[top][i])
            top+=1
            direction=1
            
        elif(direction==1):
            for i in range(top,down+1):
                # print(matrix[i][right],end=" ")
                ans.append(matrix[i][right])
            right-=1
            direction=2
            
        elif(direction==2):
            for i in range(right,left-1,-1):
                # print(matrix[down][i],end=" ")
                ans.append(matrix[down][i])
            down-=1
            direction=3
            
        elif(direction==3):
            for i in range(down,top-1,-1):
                # print(matrix[i][left],end=" ")
                ans.append(matrix[i][left])
            left+=1 
            direction=0
    return ans 


print(travereseSpirally(matrix, rows, cols))












