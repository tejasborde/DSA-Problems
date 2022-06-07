import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')

#Reverse Array
# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}

arr=[4, 5, 1, 2]
n=len(arr)


def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1
    
reverseArray(arr, 0, n-1)
print(*arr)