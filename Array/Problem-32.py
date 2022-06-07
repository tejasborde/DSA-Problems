import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# Given an array of size n and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
# 1) All elements smaller than a come first.
# 2) All elements in range a to b come next.
# 3) All elements greater than b appear in the end.
# The individual elements of three sets can appear in any order. You are required to return the modified array.



arr = [76 ,8 ,75 ,22, 59 ,96, 30, 38 ,36]
n=len(arr)
r = [44,62]

def threeWayPartition(arr,n,r):
    left=r[0]
    right=r[1]

    i=0
    j=n-1
    x=0

    while(x<=j):
        if(arr[x]<left):
            arr[i],arr[x]=arr[x],arr[i]
            i+=1
            x+=1
        elif(arr[x]>right):
            arr[j],arr[x]=arr[x],arr[j]
            j-=1
        else:
            x+=1
print("Before : ",*arr)
threeWayPartition(arr, n, r)
print("After : " ,*arr)
