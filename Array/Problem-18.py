import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')


# Count pairs with given sum

# Input:
# N = 4, K = 6
# arr[] = {1, 5, 7, 1}
# Output: 2
# Explanation: 
# arr[0] + arr[1] = 1 + 5 = 6 
# and arr[1] + arr[3] = 5 + 1 = 6.

# Input:
# N = 4, K = 2
# arr[] = {1, 1, 1, 1}
# Output: 6
# Explanation: 
# Each 1 will produce sum 2 with any 1.


# arr=[1, 5, 7, 1]
# n=len(arr)
# k=6

n,k=map(int,input().split())
arr=list(map(int,input().split()))


def countPairs(arr,n,k):
    count_dict={}
    # ans=[]
    count=0
    for i in range(n):
        temp=k-arr[i]
    
        if temp in count_dict:
            count+=count_dict[temp]
            # for j in range(count):
            #     ans.append([temp,arr[i]])
        if arr[i]  in count_dict:
            count_dict[arr[i]]+=1
        else:
            count_dict[arr[i]]=1
    # return len(ans)
    return count



print(countPairs(arr, n, k))



















