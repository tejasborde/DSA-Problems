#Find All SubArrays with sum Zero

def findSubArrays(self,arr,n):
    sumMapwithIndex={}
    
    sum=0
    ans=[]
    for i in range(n):
        
        sum+=arr[i]
        
        if(sum==0):
            ans.append([0,i])
        
        subArrays=[]
        if(sum in sumMapwithIndex):
            subArrays=sumMapwithIndex[sum]
            for x in range(len(subArrays)):
                ans.append([subArrays[x]+1,i])
        subArrays.append(i)
        sumMapwithIndex[sum]=subArrays
            
    return len(ans)