import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')



# Row with max 1s 
# Given a boolean 2D array of n x m dimensions where each 
# row is sorted. Find the 0-based index of the first row that 
# has the maximum number of 1's.


# Input: 
# N = 4 , M = 4
# Arr[][] = {{0, 1, 1, 1},
#            {0, 0, 1, 1},
#            {1, 1, 1, 1},
#            {0, 0, 0, 0}}
# Output: 2
# Explanation: Row 2 contains 4 1's (0-based
# indexing).



mat=[[0, 1, 1, 1],
     [0, 0, 1, 1],
     [1 ,1, 1, 1],
     [0, 0, 0, 0]]

rows=len(mat)
cols=len(mat[0])



#Solution 1 : BruteForce O(n^2)-TC

# def MaxOnesRow(mat,rows,cols):
#     maxOnesRow=-1
#     maxOnesCount=float('-inf')

#     for i in range(rows):
#         count=0
#         for j in range(cols):
#             if(mat[i][j]==1):
#                 count+=1
#         if(maxOnesCount<count):
#             maxOnesCount=count
#             maxOnesRow=i 
#     return maxOnesRow



#Solution 2 Using Binary Search as each row is sorted

#binary search to get the position of first one in that row
# def binarySearch(row):
#     low=0
#     high=len(row)-1

#     while(low<=high):
#         mid=low+(high-low)//2

#         if(row[mid]==1):
#             high=mid-1
#         else:
#             low=mid+1
#     return low 

# def MaxOnesRow(mat,rows,cols):
    
#     maxOnesRow=float('inf')

#     for i in range(rows):
#         startIndexOfOnes=binarySearch(mat[i])
#         if(startIndexOfOnes<=maxOnesRow):
#             maxOnesRow=i 
#     return maxOnesRow


#Solution 3 :
# using elimination of cols  and 
# go to next row if found 0 in that row

def MaxOnesRow(mat,rows,cols):
    row=-1
    col=cols-1
    for i in range(rows):
        for j in range(col,-1,-1):
            if(mat[i][j]==1):
                row=i 
                col-=1
            else:
                break
    
    return row


print(MaxOnesRow(mat, rows, cols))

















