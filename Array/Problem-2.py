import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')


arr=[3, 2, 1, 56, 10000, 167]
n=len(arr)

#Solution 1 
# def getMinMax(a,n):
#     return min(a),max(a)


#Solution 2
# def getMinMax( a, n):
#     minNo=0
#     maxNo=0
#     if(a[0]>a[-1]):
#         maxNo=a[0]
#         minNo=a[-1]
#     else:
#         maxNo=a[-1]
#         minNo=a[0]
        
#     i=0
#     j=len(a)-1
#     while(i<=j):
#         if(a[i]<minNo):
#             minNo=a[i]
#         if(a[i]>maxNo):
#             maxNo=a[i]
#         if(a[j]<minNo):
#             minNo=a[j]
#         if(a[j]>maxNo):
#             maxNo=a[j]

#         i+=1
#         j-=1
#     return minNo,maxNo



# print(getMinMax(arr, n))
