import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')

# Rearrange array in alternating positive & negative items 
# with O(1) extra space 

# Input:  arr[] = {1, 2, 3, -4, -1, 4}
# Output: arr[] = {-4, 1, -1, 2, 3, 4}

# Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
# output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}


arr=[-5, -2, -5, 2, 4, 7, 1, 8, 0, -8]
n=len(arr)

#Solution 1: If Order does not matter 
# def alternateNegativePositive(arr,n):
    
#     #Separate negative and positive in array itself 
#     i=0
#     j=n-1 

#     while(i<j):
#         if(arr[i]>=0):
#             i+=1 
#         else:
#             arr[j],arr[i]=arr[i],arr[j]
#             j-=1 
    
#     #Add alternate negative Positive
#     i=0
#     j=n-1
#     while(i<j):
#         arr[i],arr[j]=arr[j],arr[i]
#         j-=1
#         i+=2
#     print(arr)


#Solution 2 : Preserve the order of array elements
def rightRotate(arr,start,end):
    temp=arr[end]
    for i in range(end,start,-1):
        arr[i]=arr[i-1]
    arr[start]=temp



def alternateNegativePositive(arr,n):
    for i in range(n):
        if(arr[i]>0 and i%2==0):
            #Positive Number in place of Negative found
            nextNeg=None
            j=i+1
            while(j<n):
                if(arr[j]<0):
                    nextNeg=j
                    break 
                j+=1
            if(nextNeg!=None):
                rightRotate(arr, i, nextNeg)

        elif(arr[i]<0 and i%2!=0):
            #Negative Number in place of Positive found
            nextPos=None
            j=i+1
            while(j<n):
                if(arr[j]>0):
                    nextPos=j
                    break 
                j+=1
            if(nextPos!=None):
                rightRotate(arr, i, nextPos)
    print(arr)
alternateNegativePositive(arr, n)









