import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')



# Find Kth min Element  in row wise sorted matrix

mat= [[10, 20, 30, 40], 
    [15, 25, 35, 45], 
    [24, 29, 37, 48], 
    [32, 33, 39, 50]]
r=len(mat)
c=len(mat[0])
k=7




def countNumbersLessThanNumber(row,num):
    low=0
    high=len(row)-1

    while(low<=high):
        mid=(low+high)//2

        if(row[mid]<=num):
            low=mid+1
        else:
            high=mid-1
    return low

def KthElementinSortedArray(mat,r,c,k):
    low=1
    high=10**9

    while(low<=high):
        mid=(low+high)//2
        NumbersLessThanNumber=0
        for i in range(r):
            NumbersLessThanNumber+=countNumbersLessThanNumber(mat[i],mid)

        if(NumbersLessThanNumber<k):
            low=mid+1
        else:
            high=mid-1
    return low



print(KthElementinSortedArray(mat, r, c, k))