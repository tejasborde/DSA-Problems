import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')


# Sort an array of 0s, 1s and 2s 
# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.


arr=[0,1,0,2,1,0,1,2]
n=len(arr)


def sortZeroOnetwo(arr,n):
    zero=0
    two=n-1
    i=0

    while(zero<=two and i<n):
        if(arr[i]==0):
            arr[i],arr[zero]=arr[zero],arr[i]
            zero+=1
        elif(arr[i]==2):
            arr[i],arr[two]=arr[two],arr[i]
            two-=1
        else:
            i+=1 
    print(*arr)


sortZeroOnetwo(arr, n)

