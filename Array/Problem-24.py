import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# Longest consecutive subsequence
# Input:
# N = 7
# a[] = {2,6,1,9,4,5,3}
# Output:
# 6
# Explanation:
# The consecutive numbers here
# are 1, 2, 3, 4, 5, 6. These 6 
# numbers form the longest consecutive
# subsquence.


arr=[2,6,1,9,4,5,3]
n=len(arr)


#Solution 1 : O(Nlogn) to sort +O(M) to iterate
# def findLongestConseqSubseq(arr, N):
#     x=set(arr)
#     arr=list(x)
#     arr.sort()
#     max_count=0
#     count=0
#     for i in range(len(arr)-1):
#         if(arr[i]==arr[i+1]-1):
#             count+=1
#         else:
#             max_count=max(max_count,count)
#             count=0
#     max_count=max(max_count,count)
#     return max_count+1



#solution 2 : O(N)
def findLongestConseqSubseq(arr, N):
    s=set(arr)
    longestStreak=1
    for num in arr:
        if((num-1) not in s):
            streak=1
            start=num+1
            while(True):
                if((num+1) in s):
                    streak+=1
                    num+=1 
                else:
                    longestStreak=max(longestStreak,streak)
                    break
    return longestStreak

print(findLongestConseqSubseq(arr,n))