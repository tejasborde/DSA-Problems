import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')



# Longest repeating subsequence 
# https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1


# Input:
# str = "axxxy"
# Output: 2


s="aabebcdd"


#Solution 1 : Using DP

def longestRepeatingSubsequence(s):
    n=len(s)

    dp=[['' for i in range(n+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if(s[i-1]==s[j-1] and i!=j):
                # dp[i][j]=1+dp[i-1][j-1]
                dp[i][j]=dp[i-1][j-1]+s[i-1]
            else:
                # dp[i][j]=max(dp[i][j-1],dp[i-1][j])
                dp[i][j]=dp[i][j-1] if len(dp[i][j-1])>=len(dp[i-1][j]) else dp[i-1][j]
    return dp[n][n]

print(longestRepeatingSubsequence(s))
        