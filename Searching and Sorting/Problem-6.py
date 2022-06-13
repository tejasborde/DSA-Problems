#Find Missing and Repeating Element from sequence of 1 to N

def findTwoElement( self,arr, n): 
    s=set()
    expectedSum=(n*(n+1))//2
    actualSum=0
    
    repeated=0
    for i in arr:
        if(i in s):
            repeated=i
        actualSum+=i
        s.add(i)
    missingNo=expectedSum-(actualSum-repeated)
    
    
    return [repeated,missingNo]