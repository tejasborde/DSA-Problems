import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')

# Find the median
# Input: N = 5
# arr[] = 90 100 78 89 67
# Output: 89
# Explanation: After sorting the array 
# middle element is the median 


arr=[56 ,67 ,30, 79]
n=len(arr)

def findMedian(arr,n):
    arr.sort()
    if(n%2==0):
        return (arr[int(n/2)-1]+arr[int(n/2)])//2
    return arr[n//2]

print(findMedian(arr, n))












