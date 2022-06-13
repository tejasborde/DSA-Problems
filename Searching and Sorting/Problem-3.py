

import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


#Search in sorted and rotated array

class Solution:
    def findPivot(self,arr):
        for i in range(n-1):
            if(arr[i]>arr[i+1]):
                return i+1
        return 0
    def binarySearch(self,arr,l,h,key):
        mid=(l+h)//2
        
        if(l<=h):
            if(arr[mid]==key):
                return mid
            elif(arr[mid]>key):
                return self.binarySearch(arr,l,mid-1,key)
            else:
                return self.binarySearch(arr,mid+1,h,key)
        return -1
        
    def search(self, A : list, l : int, h : int, key : int):
        pivot=self.findPivot(A)
        if(pivot==h):
            return self.binarySearch(A,l,h,key)
        if(key>=A[pivot] and key<A[h]):
            return self.binarySearch(A,pivot,h,key)
        return self.binarySearch(A,l,pivot-1,key)


s=Solution()

# arr=[5 ,6, 7 ,8 ,9 ,10 ,1 ,2, 3]
# arr=[3, 5, 1, 2]
n=int(input())
arr=list(map(int,input().split()))
key=int(input())
print(s.search(arr, 0, n-1, key))