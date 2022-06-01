import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')

#right rotate by one
# Input:
# N = 5
# A[] = {1, 2, 3, 4, 5}
# Output:
# 5 1 2 3 4

# arr=[1, 2, 3, 4, 5]
arr=[9, 8, 7, 6, 4, 2, 1, 3]

def rightRotateByOne(arr):
    last=arr[-1]
    for i in range(len(arr)-1,-1,-1):
        arr[i]=arr[i-1]
    arr[0]=last
    print(*arr)

rightRotateByOne(arr)