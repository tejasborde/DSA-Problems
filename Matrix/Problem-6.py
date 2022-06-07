import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')



# Maximum size rectangle binary sub-matrix with all 1s
# Input:
# 0 1 1 0
# 1 1 1 1
# 1 1 1 1
# 1 1 0 0
# Output :
# 8
# Explanation : 
# The largest rectangle with only 1's is from 
# (1, 0) to (2, 3) which is
# 1 1 1 1
# 1 1 1 1 


mat=[[0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]
rows=len(mat)
cols=len(mat[0])

#Refer Problem-37 of Array Folder
def findMaxAreaHistogram(histogram,n):
    stack = list()

    max_area = 0 
    index = 0
    while index < len(histogram):
        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = (histogram[top_of_stack] *
                ((index - stack[-1] - 1)
                if stack else index))
            max_area = max(max_area, area)
    while stack:
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack] *
            ((index - stack[-1] - 1)
                if stack else index))

        max_area = max(max_area, area)
    return max_area



def findRectangleWithMaxOnes(mat,rows,cols):

    curHist=mat[0]
    curArea=findMaxAreaHistogram(curHist, len(curHist))

    maxArea=curArea
    for i in range(1,rows):
        for j in range(cols):
            if(mat[i][j]==0):
                curHist[j]=0
            else:
                curHist[j]+=mat[i][j]
        curArea=findMaxAreaHistogram(curHist, len(curHist))
        maxArea=max(maxArea,curArea)

    return maxArea

print(findRectangleWithMaxOnes(mat, rows, cols))








