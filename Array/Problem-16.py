#Count Inversion
# https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1

# Input: N = 5, arr[] = {2, 4, 1, 3, 5}
# Output: 3
# Explanation: The sequence 2, 4, 1, 3, 5 
# has three inversions (2, 1), (4, 1), (4, 3).

# Input: N = 5
# arr[] = {2, 3, 4, 5, 6}
# Output: 0
# Explanation: As the sequence is already 
# sorted so there is no inversion count.

import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')

arr=[2, 4, 1, 3, 5]
n=len(arr)

#Simply We have to increment counter for situation where a[i]>a[j] provided i<j


#Solution 1 : Bruteforce O(n^2)
# def countInversion(arr,n):
#     count=0
#     for i in range(n):
#         for j in range(i+1,n):
#             if(arr[i]>arr[j]):
#                 count+=1 
#     return count 



#solution 2 Using Merge Sort O(nlogn)
def merge(a,temp,left,mid,right):
    i=left 
    j=mid 
    k=left
    inv=0

    while(i<mid and j<=right):
        if(a[i]<=a[j]):
            temp[k]=arr[i]
            k+=1
            i+=1
        else:
            temp[k]=arr[j]
            k+=1
            j+=1
            inv+=mid-i

    while(i<mid):
        temp[k]=arr[i]
        k+=1
        i+=1
    while(j<=right):
        temp[k]=arr[j]
        k+=1
        j+=1
    for i in range(left,right+1):
        a[i]=temp[i]
    
    return inv
    


def mergeSort(a,temp,left,right):
    inv=0
    if(left<right):
        mid=int((left+right)/2)

        inv+=mergeSort(a, temp, left, mid)
        inv+=mergeSort(a, temp, mid+1, right)
        inv+=merge(a, temp, left, mid+1, right)
    return inv

def countInversion(arr,n):
    temp=[x for x in arr]
    count= mergeSort(arr, temp, 0, n-1)
    return count 


print(countInversion(arr, n))


