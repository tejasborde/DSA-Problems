# https://practice.geeksforgeeks.org/problems/median-of-bst/1/#


#Get Median Of BST

def countNodes(root,count):
    if(root):
        countNodes(root.left,count)
        count[0]+=1
        countNodes(root.right,count)

def getMedianNodes(root,medianNodes,k,currentIndex,even=False):
    if(root):
        getMedianNodes(root.left,medianNodes,k,currentIndex,even)
        if(even and (currentIndex[0]==k or currentIndex[0]==k-1)):
            medianNodes.append(root.data)
        elif(currentIndex==k):
            medianNodes.append(root.data)
        
        currentIndex[0]+=1
        getMedianNodes(root.right,medianNodes,k,currentIndex,even)

def findMedian(root):
    nodeCount=[0]
    countNodes(root,nodeCount)


    even=False
    if(nodeCount[0]%2==0):
        even=True
    
    medianNodes=[]

    k=nodeCount[0]/2
    currentIndex=[0]

    getMedianNodes(root, medianNodes, k, currentIndex,even)

    size=len(medianNodes)

    sum=0
    for i in medianNodes:
        sum+=i 
    
    median=sum/size 
    return median 

        
