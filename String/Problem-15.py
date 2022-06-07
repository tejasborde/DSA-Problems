import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')


# Next Greater Number i.e Next Permutation 
# Input: N = 6
# arr = {1, 2, 3, 6, 5, 4}
# Output: {1, 2, 4, 3, 5, 6}
# Explaination: The next permutation of the 
# given array is {1, 2, 4, 3, 5, 6}.

arr=[1, 2, 3, 6, 5, 4]
n=len(arr)

def nextPermutation(arr,n):

    #Traverse from right and find index(idx) such that a[idx-1]<a[idx]
    idx=-1

    for i in range(n-1,0,-1):
        if(arr[i-1]<arr[i]):
            idx=i
            break 
    
    #If the current order is last permutation i.e sorted in decrasing order then print the array in increasing order
    if(idx==-1):
        arr.sort()
        return arr 
    else:
        prev=idx 
        #Find the number greater than arr[idx-1] and closer to it
        for i in range(idx+1,n):
            if(arr[i]>arr[idx-1] and arr[i]<=arr[prev]):
                prev=i
        arr[idx-1],arr[prev]=arr[prev],arr[idx-1]

        temp=arr[idx:]
        temp=temp[::-1]
        arr[idx:]=temp 
        return arr 