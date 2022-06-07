import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# Median of two sorted arrays of different sizes


# Input: ar1[] = {-5, 3, 6, 12, 15}
#         ar2[] = {-12, -10, -6, -3, 4, 10}
# Output : The median is 3.
# Explanation : The merged array is :
#         ar3[] = {-12, -10, -6, -5 , -3,
#                  3, 4, 6, 10, 12, 15},
#        So the median of the merged array is 3


a=[2, 3, 5, 8]
b=[10, 12, 14, 16, 18, 20]
m,n=len(a),len(b)


#Solution 1 : BruteForce 
#Merege Two arrays into single array , Sort the array and Find Median

#Solution 2 : using binary Search method 

def findMedianOfSortedArrays(a,b,m,n):

    #a's length should be smaller than b
    if(m>n):
        return findMedianOfSortedArrays(b, a, n, m)

    low=0
    high=m 

    while(low<=high):
        mid=(low+high)//2
        cut1= mid
        cut2= (m+n+1)//2-mid

        l1= float('-inf') if cut1==0 else a[cut1-1]
        l2=float('-inf') if cut2==0 else b[cut2-1]

        r1=float('inf') if cut1==m else a[cut1]
        r2=float('inf') if cut2==n else b[cut2]

        if(l1<=r2 and l2<=r1):
            if((m+n)%2==0):
                return (max(l1,l2)+min(r1,r2))//2
            else:
                return max(l1,l2)
        elif(l1>r2):
            high=cut1-1
        else:
            low=cut1+1
    return 0


print(findMedianOfSortedArrays(a, b, m, n))
        