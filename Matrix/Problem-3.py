import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')



# Median in a row-wise sorted Matrix

# Input:
# R = 3, C = 3
# M = [[1, 3, 5], 
#      [2, 6, 9], 
#      [3, 6, 9]]

# Output: 5

# Explanation:
# Sorting matrix elements gives us 
# {1,2,3,3,5,6,6,9,9}. Hence, 5 is median. 

#Solution 1: Using Binary Search


# mat= [[1, 3, 5], 
#      [2, 6, 9], 
#      [3, 6, 9]]
# r=len(mat)
# c=len(mat[0])


mat= [[18], 
     [13], 
     [8], 
     [1], 
     [12], 
     [1], 
     [14], 
     [17], 
     [15], 
     [8], 
     [2]]
r=len(mat)
c=len(mat[0])

# 11 1
# 18 13 8 1 12 1 14 17 15 8 2

# 1,2,3,5,6,6,9,9

def countNumbersLessThanMid(row,target):
    low=0
    high=len(row)-1

    while(low<=high):
        mid=(low+high)//2

        if(row[mid]<=target):
            low=mid+1
        else:
            high=mid-1
    
    return low

def medianOfSortedTwoDArray(mat,r,c):

    # low=float('inf')
    # high=float('-inf')
    # for i in range(r):
    #     low=min(low,mat[i][0])
    #     high=max(low,mat[i][-1])

    low=1
    high=10**9

    while(low<=high):
        mid=(low+high)//2
        print("mid : ",mid)
        print("low : ",low,"high : ",high)
        NumbersLessThanMid=0
        for i in range(r):
            print(countNumbersLessThanMid(mat[i],mid))
            NumbersLessThanMid+=countNumbersLessThanMid(mat[i],mid)

        if(NumbersLessThanMid<=(r*c)//2):
            low=mid+1
        else:
            high=mid-1
        print()
    return low

print(medianOfSortedTwoDArray(mat, r, c))





















