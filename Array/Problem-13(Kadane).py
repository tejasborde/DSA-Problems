import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')



#Kadane's Algorithm 



#1st solution o(n^3)
# for i=0to n:
#     for j=i to n:
#         s=0
#         for k=i to j:
#             s+=arr[i]
#         mmaxSum=max(maxSum,s)

#2nd solution o(n^2) using prefix Sum Subarray
#Find PrefixSum SubArray
# pre=[]
# pre.append(0)
# for i=1 to n+1:
#     pre[i]=pre[i-1]+arr[i]
# for i to n:
#     for j=i to n:
#             s=pref[j]-pre[i-1]
#         mmaxSum=max(maxSum,s)

#3rd Solution O(n) (Kadane's Algorithm)
arr=[-1,-2,-3,-4]
n=len(arr)

def kadane(arr,n):
    maxSum=-999999
    maxTillhere=0

    for i in range(n):
        maxTillhere=maxTillhere+arr[i]
        maxSum=max(maxSum,maxTillhere)

        if(maxTillhere<0):
            maxTillhere=0
    return maxSum

print(kadane(arr, n))