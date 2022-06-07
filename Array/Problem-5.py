import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')

#Move all the negative elements to one side of the array 
# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5


# arr=list(map(int,input().split()))
arr=[-1, 2, -3, 4, 5, 6, -7, 8, 9]

def moveNegativetoStartofArr(arr):
    start=0
    negative=0
    while(start<len(arr)):
        if(arr[start]<0):
            arr[start],arr[negative]=arr[negative],arr[start]
            negative+=1
        start+=1
    return arr
    


x=moveNegativetoStartofArr(arr)
print(*x)