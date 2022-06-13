#Find First and last occurrence of number in an array
# Input:
# n=9, x=7
# arr[] = { 1, 3, 5, 5, 5, 5, 7, 123, 125 }
# Output:  6 6 

def find(arr,n,x):
    cur=0
    first=-1
    last=-1
    
    while(cur<=n-1):
        if(arr[cur]==x):
            if(first==-1):
                first=cur
                last=cur
            else:
                last=cur
        cur+=1
    return [first,last]