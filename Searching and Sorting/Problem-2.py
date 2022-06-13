#Find Value equal to index array

def valueEqualToIndex(self,arr, n):
    i=0
    size=n-1
    ans=[]
    while(i<=n-1):
        if(i+1==arr[i]):
            ans.append(i+1)
        i+=1
    return ans